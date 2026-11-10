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








