from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from login.models import Account
from candidate.models import Community, Candidate
from companion.models import Companion
User = get_user_model()
# Create your views here.


def index(request):
    a = User.objects.all()
    b = Account.objects.all()
    return HttpResponse(' this is pages')


# Common
class LoginClass(View):
    def get(self, request):
        return render(request, 'Common/login.html')





class DashboardClass(View):
    def get(self, request):
        # companions = Account.objects.filter(option = 1)
        # candidates = Account.objects.filter(option = 0)
        companions = Companion.objects.all()
        candidates = Candidate.objects.all()
        allUser = Account.objects.all()
        communities = Community.objects.all()
        print('////////////////')
        print(companions[0].MSUser.fullName)
        context = {
            'title': 'Dashboard',
            'companions': companions,
            'candidates': candidates,
            'allUser': allUser,
            'communities': communities
        }
        return render(request, 'Common/dashboard.html', context)


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
        # community = Community.objects.get(communityName = 'tu duc')
        # candidate_list = Candidate.objects.filter(community = community)
        candidate_list = Candidate.objects.all()
        print('////////////////////////')
        print(candidate_list)
        print(request.user)
        title = 'Candidates'
        context = {
            'title': title,
            'candidate_list': candidate_list
            }
        return render(request, 'Candidate/candidate_list.html', context)
class CompanionCandidateListClass(View):
    def get(self, request):
        community = Community.objects.get(communityName = 'tu duc')
        candidate_list = Candidate.objects.filter(community = community)
        print('////////////////////////')
        print(candidate_list)
        title = 'Candidates'
        context = {
            'title': title,
            'candidate_list': candidate_list
            }
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
        all_community = Community.objects.all()
        title = 'Communities'
        community_list = []
        for community in all_community:
            candidateEachCom = Candidate.objects.filter( community = community)
            print('//////////////////////////////?????????')
            print(community.patron.month)
            detail_Community = {
                'community': community,
                'amout_candidate': candidateEachCom.__len__()
            }
            community_list.append(detail_Community)
        context = {
            'community_list':community_list,
            'title': title
            }
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
# class CommunityGroupListClass(View):
#     def get(self, request):
#         title = 'Community Groups'
#         context = {'title': title}
#         return render(request, 'CommunityGroup/community_group_list.html', context)
#
#
# class AddCommunityGroupClass(View):
#     def get(self, request):
#         title = 'Add Community Group'
#         context = {'title': title}
#         return render(request, 'CommunityGroup/add_community_group.html', context)
#
#
# class EditCommunityGroupClass(View):
#     def get(self, request):
#         title = 'Edit Community Group'
#         context = {'title': title}
#         return render(request, 'CommunityGroup/edit_community_group.html', context)


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


# Companion Report
class CompanionReportListClass(View):
    def get(self, request):
        title = 'Companion Reports'
        context = {'title': title}
        return render(request, 'CompanionReport/companion_report_list.html', context)


class AddCompanionReportClass(View):
    def get(self, request):
        title = 'Add Companion Report'
        context = {'title': title}
        return render(request, 'CompanionReport/add_companion_report.html', context)


class EditCompanionReportClass(View):
    def get(self, request):
        title = 'Edit Companion Report'
        context = {'title': title}
        return render(request, 'CompanionReport/edit_companion_report.html', context)