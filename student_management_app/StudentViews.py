import datetime
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from student_management_app.models import Students, Courses, Subjects, CustomUser, Attendance, AttendanceReport, \
    LeaveReportStudent, FeedBackStudent, NotificationStudent


def student_home(req):
    student_obj=Students.objects.get(admin=req.user.id)
    attendance_total=AttendanceReport.objects.filter(student_id=student_obj).count()
    attendance_present=AttendanceReport.objects.filter(student_id=student_obj,status=True).count()
    attendance_absent=AttendanceReport.objects.filter(student_id=student_obj,status=False).count()
    course=Courses.objects.get(id=student_obj.course_id.id)
    subjects=Subjects.objects.filter(course_id=course).count()

    subject_name=[]
    data_present=[]
    data_absent=[]
    subject_data=Subjects.objects.filter(course_id=student_obj.course_id)
    for subject in subject_data:
        attendance=Attendance.objects.filter(subject_id=subject.id)
        attendance_present_count=AttendanceReport.objects.filter(attendance_id__in=attendance,status=True,student_id=student_obj.id).count()
        attendance_absent_count=AttendanceReport.objects.filter(attendance_id__in=attendance,status=False,student_id=student_obj.id).count()
        subject_name.append(subject.subject_name)
        data_present.append(attendance_present_count)
        data_absent.append(attendance_absent_count)

    return render(req,"student_template/student_home_template.html",{"total_attendance":attendance_total,"attendance_absent":attendance_absent,"attendance_present":attendance_present,"subjects":subjects,"data_name":subject_name,"data1":data_present,"data2":data_absent})

def student_view_attendance(req):
    student=Students.objects.get(admin=req.user.id)
    course=student.course_id
    subjects=Subjects.objects.filter(course_id=course)
    return render(req,"student_template/student_view_attendance.html",{"subjects":subjects})

def student_view_attendance_post(req):
    subject_id=req.POST.get("subject")
    start_date=req.POST.get("start_date")
    end_date=req.POST.get("end_date")

    start_data_parse=datetime.datetime.strptime(start_date,"%Y-%m-%d").date()
    end_data_parse=datetime.datetime.strptime(end_date,"%Y-%m-%d").date()
    subject_obj=Subjects.objects.get(id=subject_id)
    user_object=CustomUser.objects.get(id=req.user.id)
    stud_obj=Students.objects.get(admin=user_object)

    attendance=Attendance.objects.filter(attendance_date__range=(start_data_parse,end_data_parse),subject_id=subject_obj)
    attendance_reports=AttendanceReport.objects.filter(attendance_id__in=attendance,student_id=stud_obj)
    return render(req,"student_template/student_attendance_data.html",{"attendance_reports":attendance_reports})

def student_apply_leave(req):
    staff_obj = Students.objects.get(admin=req.user.id)
    leave_data=LeaveReportStudent.objects.filter(student_id=staff_obj)
    return render(req,"student_template/student_apply_leave.html",{"leave_data":leave_data})

def student_apply_leave_save(req):
    if req.method!="POST":
        return HttpResponseRedirect(reverse("student_apply_leave"))
    else:
        leave_date=req.POST.get("leave_date")
        leave_msg=req.POST.get("leave_msg")

        student_obj=Students.objects.get(admin=req.user.id)
        try:
            leave_report=LeaveReportStudent(student_id=student_obj,leave_date=leave_date,leave_message=leave_msg,leave_status=0)
            leave_report.save()
            messages.success(req, "Successfully Applied for Leave")
            return HttpResponseRedirect(reverse("student_apply_leave"))
        except:
            messages.error(req, "Failed To Apply for Leave")
            return HttpResponseRedirect(reverse("student_apply_leave"))


def student_feedback(req):
    staff_id=Students.objects.get(admin=req.user.id)
    feedback_data=FeedBackStudent.objects.filter(student_id=staff_id)
    return render(req,"student_template/student_feedback.html",{"feedback_data":feedback_data})

def student_feedback_save(req):
    if req.method!="POST":
        return HttpResponseRedirect(reverse("student_feedback"))
    else:
        feedback_msg=req.POST.get("feedback_msg")

        student_obj=Students.objects.get(admin=req.user.id)
        try:
            feedback=FeedBackStudent(student_id=student_obj,feedback=feedback_msg,feedback_reply="")
            feedback.save()
            messages.success(req, "Successfully Sent Feedback")
            return HttpResponseRedirect(reverse("student_feedback"))
        except:
            messages.error(req, "Failed To Send Feedback")
            return HttpResponseRedirect(reverse("student_feedback"))

def student_profile(req):
    user=CustomUser.objects.get(id=req.user.id)
    student=Students.objects.get(admin=user)
    return render(req,"student_template/student_profile.html",{"user":user,"student":student})

def student_profile_save(req):
    if req.method!="POST":
        return HttpResponseRedirect(reverse("student_profile"))
    else:
        first_name=req.POST.get("first_name")
        last_name=req.POST.get("last_name")
        password=req.POST.get("password")
        address=req.POST.get("address")
        try:
            customuser=CustomUser.objects.get(id=req.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            if password!=None and password!="":
                customuser.set_password(password)
            customuser.save()

            student=Students.objects.get(admin=customuser)
            student.address=address
            student.save()
            messages.success(req, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("student_profile"))
        except:
            messages.error(req, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("student_profile"))

@csrf_exempt
def student_fcmtoken_save(req):
    token=req.POST.get("token")
    try:
        student=Students.objects.get(admin=req.user.id)
        student.fcm_token=token
        student.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")

def studentAllNotification(req):
    student=Students.objects.get(admin=req.user.id)
    notifications=NotificationStudent.objects.filter(student_id=student.id)
    return render(req,"student_template/all_notification.html",{"notifications":notifications})