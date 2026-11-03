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








