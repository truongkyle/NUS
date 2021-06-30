from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.


def index(request):
    return HttpResponse(' this is pages')


# Common
class LoginClass(View):
    def get(self, request):
        return render(request, 'Common/login.html')


class DashboardClass(View):
    def get(self, request):
        return render(request, 'Common/dashboard.html', {'title': 'Dashboard'})


# User
class ChangePasswordClass(View):
    def get(self, request):
        context = {'title': 'Change Password'}
        return render(request, 'User/change_password.html', context)


class UserInfoClass(View):
    def get(self, request):
        title = 'Personal Info'
        status_image = 0
        role_user = 'Candidate'
        context = {'title': title, 'status_image': status_image, 'role_user': role_user}
        return render(request, 'User/info_user.html', context)


# Manager
class ManagerListClass(View):
    def get(self, request):
        title = 'Managers'
        context = {'title': title}
        return render(request, 'Manager/manager_list.html', context)


class AddManagerClass(View):
    def get(self, request):
        title = 'Add Manager'
        context = {'title': title}
        return render(request, 'Manager/add_manager.html', context)


class EditManagerClass(View):
    def get(self, request):
        title = 'Edit Manager'
        context = {'title': title}
        return render(request, 'Manager/edit_manager.html', context)


# Candidate
class CandidateListClass(View):
    def get(self, request):
        title = 'Candidates'
        context = {'title': title}
        return render(request, 'Candidate/candidate_list.html', context)


class AddCandidateClass(View):
    def get(self, request):
        title = 'Add Candidate'
        context = {'title': title}
        return render(request, 'Candidate/add_candidate.html', context)


class EditCandidateClass(View):
    def get(self, request):
        title = 'Edit Candidate'
        context = {'title': title}
        return render(request, 'Candidate/edit_candidate.html', context)


# Community
class CommunityListClass(View):
    def get(self, request):
        title = 'Communities'
        context = {'title': title}
        return render(request, 'Community/community_list.html', context)


class AddCommunityClass(View):
    def get(self, request):
        title = 'Add Community'
        context = {'title': title}
        return render(request, 'Community/add_community.html', context)


class EditCommunityClass(View):
    def get(self, request):
        title = 'Edit Community'
        context = {'title': title}
        return render(request, 'Community/edit_community.html', context)


# Companion
class CompanionListClass(View):
    def get(self, request):
        title = 'Companions'
        context = {'title': title}
        return render(request, 'Companion/companion_list.html', context)


class AddCompanionClass(View):
    def get(self, request):
        title = 'Add Companion'
        context = {'title': title}
        return render(request, 'Companion/add_companion.html', context)


class EditCompanionClass(View):
    def get(self, request):
        title = 'Edit Companion'
        context = {'title': title}
        return render(request, 'Companion/edit_companion.html', context)


# Spiritual Guide
class SpiritualGuideListClass(View):
    def get(self, request):
        title = 'Spiritual Guides'
        context = {'title': title}
        return render(request, 'SpiritualGuide/spiritual_guide_list.html', context)


class AddSpiritualGuideClass(View):
    def get(self, request):
        title = 'Add Spiritual Guide'
        context = {'title': title}
        return render(request, 'SpiritualGuide/add_spiritual_guide.html', context)


class EditSpiritualGuideClass(View):
    def get(self, request):
        title = 'Edit Spiritual Guide'
        context = {'title': title}
        return render(request, 'SpiritualGuide/edit_spiritual_guide.html', context)


# Community Group
class CommunityGroupListClass(View):
    def get(self, request):
        title = 'Community Groups'
        context = {'title': title}
        return render(request, 'CommunityGroup/community_group_list.html', context)


class AddCommunityGroupClass(View):
    def get(self, request):
        title = 'Add Community Group'
        context = {'title': title}
        return render(request, 'CommunityGroup/add_community_group.html', context)


class EditCommunityGroupClass(View):
    def get(self, request):
        title = 'Edit Community Group'
        context = {'title': title}
        return render(request, 'CommunityGroup/edit_community_group.html', context)


# Teacher
class TeacherListClass(View):
    def get(self, request):
        title = 'Teachers'
        context = {'title': title}
        return render(request, 'Teacher/teacher_list.html', context)


class AddTeacherClass(View):
    def get(self, request):
        title = 'Add Teacher'
        context = {'title': title}
        return render(request, 'Teacher/add_teacher.html', context)


class EditTeacherClass(View):
    def get(self, request):
        title = 'Edit Teacher'
        context = {'title': title}
        return render(request, 'Teacher/edit_teacher.html', context)


# Timetable
class TimetableListClass(View):
    def get(self, request):
        title = 'Timetable'
        context = {'title': title}
        return render(request, 'Timetable/timetable_list.html', context)


class AddTimetableClass(View):
    def get(self, request):
        title = 'Add Timetable'
        context = {'title': title}
        return render(request, 'Timetable/add_timetable.html', context)


class EditTimetableClass(View):
    def get(self, request):
        title = 'Edit Timetable'
        context = {'title': title}
        return render(request, 'Timetable/edit_timetable.html', context)


# Department
class DepartmentListClass(View):
    def get(self, request):
        title = 'Departments'
        context = {'title': title}
        return render(request, 'Department/department_list.html', context)


class AddDepartmentClass(View):
    def get(self, request):
        title = 'Add Department'
        context = {'title': title}
        return render(request, 'Department/add_department.html', context)


class EditDepartmentClass(View):
    def get(self, request):
        title = 'Edit Department'
        context = {'title': title}
        return render(request, 'Department/edit_department.html', context)