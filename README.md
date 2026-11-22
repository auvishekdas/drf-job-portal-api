# Django Job Portal API

Welcome to the **Django Job Portal API** project! This is a modern backend web application built using Python, Django, and Django REST Framework (DRF).

## 🛠️ Tech Stack
- **Language:** Python
- **Framework:** Django & DRF
- **Version Control:** Git & GitHub

## 📝 Today's Progress (Day 01)
- Created Django project (`Jobportal`) and app (`Job`).
- Configured virtual environment (`venv`).
- Set up `.gitignore` and organized static/template folders.
- Successfully ran the local development server and tested the base view.

## 📝 Today's Progress (Day 02)
- Updated the browser tab title to **"International Job Portal"** in the navigation template.
- Implemented styled main text headings with **"International Job Portal"** in distinct colors (purple and black) within the UI.
- Implemented Bootstrap grid system (`container`, `row`, `col-sm-4`) for a responsive layout.
- Successfully integrated static images and Font Awesome social media icons (Twitter, Facebook, Instagram, LinkedIn) into the layout.
- Tested and verified the updated frontend design locally on the development server.

## 📝 Today's Progress (Day 03)
- Navigation Bar Design & UI Customization
- Designed and structured a responsive navigation bar (`navigation.html`) using Bootstrap 4.
- Added essential menu links (Home, Jobs, User Login, Recruiter Login, Admin Login, Contact) in a single horizontal line.
- Integrated Font Awesome icons for all navigation items to enhance UI aesthetics.
- Applied custom CSS styling with `white-space: nowrap` and smooth hover effects (background color change, rounded corners, and bold text).

## 📝 Today's Progress (Day 04)
- Homepage Body Design & Placed Candidates Section
- Designed and structured the homepage (`index.html`) extending the base layout and integrating the navigation component.
- Added a full-width promotional banner image (`container-fluid`) at the top of the homepage.
- Developed an "Our Placed Candidates" section utilizing Bootstrap grid system (`container`, `row`, `col-md-3`).
- Styled candidate profile images into circular avatars using `border-radius: 50%` with absolute positioned caption overlays.
- Tested and verified the updated frontend UI design locally on the development server.

## 📝 Today's Progress (Day 05)
- **Login Pages Creation:** Created separate HTML templates for Admin, Recruiter, and User logins.
- **Navigation Integration:** Added smooth routing links for all login pages inside `navigation.html`.
- **Views & URLs Configuration:** Configured respective view functions in `views.py` and mapped clean URL routes in `urls.py`.
- **Security & Styling:** Implemented Django CSRF protection in forms and styled the UI components locally.
- **Local Testing:** Verified all login interfaces successfully on the local development server.

## 📝 Today's Progress (Day 06)
- **Footer Component Creation:** Created a dedicated `footer.html` template file to maintain a clean and modular layout structure across the Django job portal project.
- **Styling & Layout Structure:** Implemented a custom black background with 100% width and a fixed height, integrating responsive Bootstrap grid components (`container`, `row`, `col-md-4`).
- **Contact Info & Icon Integration:** Added a "Contact Information" section featuring a stylized map marker icon (`fa-map-marker`) and custom inline CSS styling (`color: chartreuse; font-size: 18px;`).
- **Template Inclusion:** Successfully rendered and integrated `footer.html` into the main `index.html` layout using Django's template inclusion tag (`{% include 'footer.html' %}`).
- **Local Testing:** Verified the updated footer UI design and responsiveness locally on the development server to ensure visual accuracy.

## 📝 Today's Progress (Day 07)
- **Comprehensive Footer Design & UI Enhancement:** Updated the `footer.html` component into a structured 3-column layout featuring Contact Information (location, email, phone, and GitHub links), International Job Placement details, and a functional Newsletter subscription form with custom styling.
- **Template Inclusion:** Successfully rendered and integrated `footer.html` into application layout templates (including `user_login.html`) using Django's template inclusion tag (`{% include 'footer.html' %}`).
- **Local Testing & Verification:** Verified the updated layout, responsiveness, and visual alignment successfully on the local development server (`localhost:8000`).

## 📝 Today's Progress (Day 08)
- **Database Migration & Setup:** Executed database migration commands (`python manage.py migrate`) to apply and update the required table schemas locally.
- **Superuser Account Creation:** Created a secure superuser account (`python manage.py createsuperuser`) with designated username and credentials for administrative access.
- **Admin Dashboard Authentication & Testing:** Successfully logged into the Django administration panel (`/admin/`) using the superuser credentials and verified the authentication and user management interface (`Groups` and `Users`) on the local development server (`localhost:8000`).

## 📝 Today's Progress (Day 09)
- **Candidate User Model Creation (`models.py`):** Developed the `CandidateUser` model linked with Django's built-in `User` model via a ForeignKey, adding essential fields including `mobile`, `image`, `gender`, and `type` with a string representation (`__str__`).
- **Admin Panel Registration (`admin.py`):** Registered the `CandidateUser` model successfully within the Django administration module to manage candidate data seamlessly.
- **Admin Dashboard Testing & Verification:** Verified the updated database models on the local development server (`localhost:8000/admin/`), ensuring the `Candidate users` section and input forms render and function correctly.

## 📝 Today's Progress (Day 10)
- **User Login UI Enhancement (`user_login.html`):** Added a "Create an account" button alongside the login form, linking it dynamically to the signup route using Django template tags (`{% url 'user_signup' %}`).
- **User Signup Page Integration & Routing (`views.py` & `urls.py`):** Configured the `user_signup` view function and established the respective URL routing path to seamlessly transition from the login page to the signup interface.
- **Interactive Signup Form Design (`user_signup.html`):** Developed a responsive signup template with navigation, custom marquee styling, and bootstrap grid input fields for "First Name" and "Last Name", successfully enabling users to navigate from login and access the complete signup view on the local server (`localhost:8000/user_signup`).

## 📝 Today's Progress (Day 11)
- **Comprehensive Signup Form Expansion (`user_signup.html`):** Enhanced the registration template by adding dedicated input fields for Contact Number, Email Address, Password, and Confirm Password within a structured bootstrap grid layout.
- **Interactive Gender & File Upload Fields (`user_signup.html`):** Implemented custom inline radio buttons for gender selection (Male/Female) with styled borders and integrated a file upload field for profile images (`enctype="multipart/form-data"`).
- **UI Layout & Form Alignment Fixed:** Refined the HTML structural tags, resolving overlapping issues and ensuring a clean, responsive, and professional user interface presentation on the local development server (`localhost:8000/user_signup`).

## 📝 Today's Progress (Day 12)
- **Mandatory Field Validation (`required`):** Implemented the `required` attribute across all essential signup form input fields to ensure users cannot submit empty values.
- **Client-Side Password Matching (JavaScript):** Integrated a custom JavaScript validation function (`checkpass()`) to verify that the Password and Confirm Password fields match prior to form submission, triggering an alert and focusing on the confirm field upon a mismatch.
- **Contact Number Input Optimization (`type="tel"`):** Configured the contact number field with `type="tel"` to trigger optimal numeric keypads on mobile devices and refined form interactivity.
- **Local Server Testing & Verification:** Successfully tested and verified the signup form layout, inline JavaScript validation alerts, and input functionalities on the local development server (`localhost:8000/user_signup`).

## 📝 Today's Progress (Day 13)
- **OS Module Import (`settings.py`):** Imported the built-in Python `os` module at the top of the settings file to manage directory paths dynamically.
- **Media Settings Configuration (`settings.py`):** Configured `MEDIA_URL = '/media/'` and `MEDIA_ROOT = os.path.join(BASE_DIR, 'media')` to properly store and handle uploaded user files and profile images.
- **Media URL Routing (`urls.py`):** Imported `settings` and `static` utility functions, and extended `urlpatterns` with `+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` to serve media files during development.
- **Local Server Testing & Verification:** Successfully tested and verified the backend settings and media handling configuration on the local development server.

## 📝 Today's Progress (Day 14)
- **User Signup Workflow Completion:** Successfully implemented and debugged the complete user registration workflow from frontend to backend.
- **Form Data & File Handling (`views.py`):** Handled `POST` requests and profile image uploads securely using `request.POST.get()` and `request.FILES`, resolving `MultiValueDictKeyError` issues.
- **Database Object Creation:** Integrated Django's built-in `User.objects.create_user()` with custom candidate creation logic to store user credentials and files safely.
- **Template Modernization (`user_signup.html`):** Updated legacy `ifequal` tags to modern Django `if` conditional tags and added `enctype="multipart/form-data"` to the form.
- **JavaScript Alerts & Redirection:** Configured popup success notifications (`alert("Signup Successful")`) and automated redirection to the login page (`user_login`).
- **End-to-End Testing & Verification:** Successfully tested, debugged, and verified the entire user signup process on the local development server (`localhost:8000/user_signup`).

## 📝 Today's Progress (Day 15)
- **User Login Authentication (`views.py`):** Successfully implemented the `user_login_request` view using Django's built-in `authenticate()` and `login()` functions to verify user credentials securely.
- **Candidate User Verification & Exception Handling:** Integrated `try-except` blocks and `Candidateuser` model queries to ensure that only registered candidates can log in, handling invalid inputs gracefully.
- **Secure Dashboard Access (`user_home`):** Created the `user_home` view and protected it with `request.user.is_authenticated` to prevent unauthorized direct URL access.
- **Dynamic JavaScript Alerts & Redirection (`user_login.html`):** Configured conditional template tags (`{% if error %}`) to trigger browser alert notifications (`Login Successful` or `Invalid Login Credentials`) and automated redirection using `window.location`.
- **URL Routing & Template Setup:** Added the `user_home` path in `urls.py` and structured the `user_home.html` template extending navigation bars and static blocks.
- **Local Server Testing & Verification:** Successfully tested and verified the complete login flow and secure redirection on the local development server (`localhost:8000/user_login`).

## 📝 Today's Progress (Day 16)
- **User Navigation Bar (`user_navigation.html`):** Created a dedicated, customized navigation bar for authenticated users featuring `Home`, `Job List`, `Change Password`, and `Logout` options with appropriate icons.
- **Template Integration (`user_home.html`):** Successfully integrated and included the `user_navigation.html` component into the user dashboard layout for seamless navigation.
- **User Logout Functionality (`views.py`):** Implemented the `logout_request` view leveraging Django's built-in `logout()` function to securely terminate user sessions.
- **URL Routing Configuration (`urls.py`):** Configured the dedicated URL path for the logout feature (`path('logout/', logout_request, name='logout')`).
- **Session Flow & Dashboard Verification:** Verified the complete authentication cycle where successful login directs users to the protected `user_home` dashboard displaying all features (Home, Job List, Change Password, and Logout), and clicking logout safely terminates the session, redirecting back to the local server's public home page output (`localhost:8000`).

## 📝 Today's Progress (Day 17)
- **Recruiter Signup Template (`recruiter_signup.html`):** Created the recruiter registration page by adapting the user signup layout with `{% load static %}`, `{% block body %}`, `{% include 'navigation.html' %}`, and `{% include 'footer.html' %}`, along with a marquee header (`Recruiter Signup`), CSRF token, form fields (`First Name`, `Last Name`, `Contact Number`, `Company`, `Email Address`, `Password`, `Confirm Password`, `Gender`, `Image`), and submit button.
- **Client-Side Validation & Alert Handling (`recruiter_signup.html`):** Added JavaScript password matching validation (`document.signup.password` check returning `false` on mismatch or `true` on match) and conditional template alerts (`error == "no"` showing `Signup Successful` with redirect to user login, and `error == "yes"` showing `Something went wrong, please try again`).
- **Recruiter Login Link Integration (`recruiter_login.html`):** Updated the recruiter login page with `{% url 'recruiter_signup' %}` so recruiters can navigate directly to the signup page from the login screen.
- **Recruiter Model Definition (`models.py`):** Defined the `Recruiter` model inheriting from `models.Model` with fields for `user`, `mobile`, `image`, `gender`, `company`, `type`, and `status`.
- **Recruiter Signup View (`views.py`):** Implemented the `recruiter_signup` view handling `POST` requests to extract form data (`f_name`, `l_name`, `password`, `email`, `contact`, `gender`, `company`) and uploaded files (`request.FILES.get('image')`), creating the Django `User` and `Recruiter` records inside a `try-except` block and rendering `recruiter_signup.html`.
- **URL Routing & Local Verification (`urls.py`):** Configured `path('recruiter_signup/', views.recruiter_signup, name='recruiter_signup')` and verified the rendered `localhost:8000/recruiter_login` and `localhost:8000/recruiter_signup` pages on the local development server.

## 📝 Today's Progress (Day 18)
- **Recruiter Home Template (`recruiter_home.html`):** Created the recruiter dashboard template using `{% load static %}`, `{% block body %}`, `{% include 'user_navigation.html' %}`, and `{% endblock %}` to structure the authenticated recruiter view.
- **Pending Status Alert (`recruiter_login.html`):** Added conditional template alert handling (`error == "not"` / pending status) rendering `<script>alert("Your Login Status is Pending");</script>` inside the template block.
- **Admin Model Registration (`admin.py`):** Registered the recruiter user model in Django admin using `admin.site.register(recruiter_user)` so recruiter accounts and approval status can be managed from the admin panel.
- **Recruiter Home & Login Views (`views.py`):** Implemented `recruiter_home` with `request.user.is_authenticated` check (redirecting unauthenticated users to `recruiter-login` and rendering the recruiter home template), and updated `recruiter_login` to authenticate credentials, verify `user1.type == 'recruiter'` and `user1.status != 'pending'`, log in approved users, or set status/error messages (`Not accepted` / `Invalid user`).
- **End-to-End Flow Verification:** Tested recruiter signup (`localhost:8000/recruiter_signup`) showing `"Signup Successful"`, followed by recruiter login (`localhost:8000/recruiter_login`) displaying `"Your Login Status is Pending"` for unapproved accounts.

## 📝 Today's Progress (Day 19)
- **Admin Home & Navigation Templates (`admin_home.html`, `admin_navigation.html`, `view_users.html`):** Built the admin navigation bar (`Home`, `New_Recruiter_Request`, `View Recruiters`, `View Users`, `Change Password`, `Logout`) and integrated it into `admin_home.html` and `view_users.html` using `{% load static %}` and `{% include %}`.
- **Admin Login Feedback & Redirect (`admin_login.html`):** Added conditional template handling to display `"Login Successful"` and redirect to `admin_home` on valid login (`error == "no"`), or show `"Invalid Login Credentials, Please Try Again"` on failure (`error == "yes"`).
- **Admin Authentication & Routing (`views.py`, `urls.py`):** Configured the `admin_home` URL route and implemented `admin_login` with `authenticate()`, `user.is_staff` check, and `login()` session handling.
- **End-to-End Verification:** Verified admin login at `localhost:8000/admin_login` (`"Login Successful"`) and redirection to `localhost:8000/admin_home`.

## 📝 Today's Progress (Day 20)
- **Admin Navigation Link (`admin_navigation.html`):** Linked the `View Users` menu item to `{% url 'view_users' %}` for direct navigation from the admin panel.
- **View Users Routing & Authentication (`urls.py`, `views.py`):** Configured the `view_users` route and implemented `view_users` with `request.user.is_authenticated` check and `CandidateUser.objects.all()` data query.
- **Candidate Users Table (`view_users.html`):** Rendered candidate records in a table layout (`S.No.`, `Full Name`, `Email ID`, `Contact`, `Gender`, `Image`, `Action`) using `{% for i in data %}`.
- **Signup & Model Field Alignment (`user_signup.html`, `views.py`, `models.py`):** Standardized `mobile` field naming across signup input, view creation (`CandidateUser.objects.create`), and model definition so candidate contact numbers render accurately.
- **End-to-End Verification:** Logged in via `admin_login`, navigated to `view_users`, and verified candidate user rows including contact numbers display properly.

## 📝 Today's Progress (Day 21)
- **DataTables Export Integration (`view_users.html`):** Integrated DataTables buttons (Copy, Excel, CSV, PDF) and layout structure into the candidate users view.
- **CDN & Script Sequencing (`view_users.html`):** Properly ordered DataTables CSS, JS, export extension libraries (`jszip`, `pdfmake`), and initialization script (`new DataTable('#example', ...)`) after the table element.
- **Table Interactivity & UI:** Enabled live search, pagination, and file export functionalities on the `id="example"` candidate table.
- **End-to-End Verification:** Verified that the export buttons, search bar, and data rows render and function correctly on the `view_users` page.

## 📝 Today's Progress (Day 22)
- **Delete Action Link (`view_users.html`):** Added a delete link (`{% url 'delete_user' i.id %}`) in the `Action` column for each candidate user row.
- **Delete Route & View (`urls.py`, `views.py`):** Configured `path('delete_user/<int:pid>/', delete_user, name="delete_user")` and implemented `delete_user(request, pid)` with authentication check (`request.user.is_authenticated`), `CandidateUser.objects.get(id=pid)`, `.delete()`, and redirect to `view_users`.
- **Table Row Styling (`view_users.html`):** Updated table row styling (`background-color: cornflowerblue; color: ghostwhite`) so user records appear clearly.
- **End-to-End Verification:** Tested deleting a candidate user from `view_users` and confirmed the record is removed and the table updates cleanly.

## 📝 Today's Progress (Day 23)
- **Delete Confirmation (`view_users.html`):** Added a confirmation prompt (`Are You Agree?`) before executing user deletion to prevent accidental removals.
- **Recruiters Dropdown & Pending Route (`admin_navigation.html`, `urls.py`, `views.py`):** Added a `Recruiters` dropdown menu (`Pending`, `Accepted`, `Rejected`, `All Recruiter`), configured the `recruiter_pending` route and view filtering `RecruiterUser` records with `status='pending'`, and fixed template tag syntax and browser cache issues that caused a 404 error.
- **Pending Recruiters Table (`recruiter_pending.html`):** Built the pending recruiters table layout with fields including serial number, full name, email ID, contact, gender, company, image, and action.
- **Field & Variable Mapping Fix (`views.py`):** Resolved a duplicate variable name (`c`) in `recruiter_signup` where `company` was overwriting `mobile`, ensuring contact numbers and company names store separately.
- **Recruiter Delete Workflow (`views.py`, `urls.py`, `recruiter_pending.html`):** Added `delete_recruiter(request, pid)` and `delete_recruiter/<int:pid>/` using `RecruiterUser` so recruiter deletions no longer trigger `CandidateUser` `DoesNotExist` errors.

## 📝 Today's Progress (Day 24)
- **Status Column & Display (`recruiter_pending.html`):** Added the `Status` column header (`<th>Status</th>`) and bound `{{i.status}}` inside the table row so pending recruiter status displays clearly.
- **End-to-End Verification:** Ran the application and confirmed that recruiter records in the pending recruiters table properly display the `pending` status.







