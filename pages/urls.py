from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.index, name='Pages'),
    # Common
    path('login/', views.LoginClass.as_view(), name='login'),
    path('dashboard/', views.DashboardClass.as_view(), name='dashboard'),
    # User
    path('change-password/', views.ChangePasswordClass.as_view(), name='change_password'),
    path('user-info/', views.UserInfoClass.as_view(), name='user_info'),
    # Manager
    path('manager-list/', views.ManagerListClass.as_view(), name='manager_list'),
    path('add-manager/', views.AddManagerClass.as_view(), name='add_manager'),
    path('edit-manager/', views.EditManagerClass.as_view(), name='edit_manager'),
    # Candidate
    path('candidate-list/', views.CandidateListClass.as_view(), name='candidate_list'),
    path('add-candidate/', views.AddCandidateClass.as_view(), name='add_candidate'),
    path('edit-candidate/', views.EditCandidateClass.as_view(), name='edit_candidate'),
    # Community
    path('community-list/', views.CommunityListClass.as_view(), name='community_list'),
    path('add-community/', views.AddCommunityClass.as_view(), name='add_community'),
    path('edit-community/', views.EditCommunityClass.as_view(), name='edit_community'),
    # Companion
    path('companion-list/', views.CompanionListClass.as_view(), name='companion_list'),
    path('add-companion/', views.AddCompanionClass.as_view(), name='add_companion'),
    path('edit-companion/', views.EditCompanionClass.as_view(), name='edit_companion'),
    # Spiritual Guide
    path('spiritual-guide-list/', views.SpiritualGuideListClass.as_view(), name='spiritual_guide_list'),
    path('add-spiritual-guide/', views.AddSpiritualGuideClass.as_view(), name='add_spiritual_guide'),
    path('edit-spiritual-guide/', views.EditSpiritualGuideClass.as_view(), name='edit_spiritual_guide'),
    # Community Group
    path('community-group-list/', views.CommunityGroupListClass.as_view(), name='community_group_list'),
    path('add-community-group/', views.AddCommunityGroupClass.as_view(), name='add_community_group'),
    path('edit-community-group/', views.EditCommunityGroupClass.as_view(), name='edit_community_group'),
    # Teacher
    path('teacher-list/', views.TeacherListClass.as_view(), name='teacher_list'),
    path('add-teacher/', views.AddTeacherClass.as_view(), name='add_teacher'),
    path('edit-teacher/', views.EditTeacherClass.as_view(), name='edit_teacher'),
    # Timetable
    path('timetable/', views.TimetableListClass.as_view(), name='timetable'),
    path('add-timetable/', views.AddTimetableClass.as_view(), name='add_timetable'),
    path('edit-timetable/', views.EditTimetableClass.as_view(), name='edit_timetable'),
    # Department
    path('department_list/', views.DepartmentListClass.as_view(), name='department_list'),
    path('add-department/', views.AddDepartmentClass.as_view(), name='add_department'),
    path('edit-department/', views.EditDepartmentClass.as_view(), name='edit_department'),
]
