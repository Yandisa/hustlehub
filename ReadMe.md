# HustleHub 🛒

**HustleHub** is a dynamic online marketplace built for local entrepreneurs and hustlers. Post, browse, and buy products or services with ease in a sleek, modern platform built with Django and Bootstrap.

🌐 **Live Demo**: [https://hustlehub-7lk9.onrender.com](https://hustlehub-7lk9.onrender.com)
📁 **GitHub**: [https://github.com/Yandisa/hustlehub](https://github.com/Yandisa/hustlehub)

---

## 📚 Table of Contents
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Screenshots](#-screenshots)
- [Future Features](#-future-features)
- [Credits](#-credits)
- [License](#-license)
- [Docker Setup](#-docker-setup)
- [Developer Documentation](#-developer-documentation)

---

## 🔥 Features

- 🧍 User Authentication (Register/Login/Logout)
- 📦 Post Listings (Products/Services)
- 📄 View and Manage Your Listings
- 💬 Contact Sellers
- 🔍 Search and Filter by Category
- 📸 Upload Product Images
- 📱 Fully Responsive Design

---

## 🎨 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Bootstrap 5, HTML, CSS
- **Database:** SQLite (default, easy setup)
- **Icons:** Font Awesome
- **Fonts:** Poppins + Space Mono

---

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Yandisa/hustlehub.git
   cd hustlehub
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate     # On Windows
   # OR
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. Open your browser and visit:  
   [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📸 Screenshots

### Homepage
![Homepage](screenshots/home_page.png)

### Login Page
![Login](screenshots/products.png)

### Footer
![Footer](screenshots/footer.png)

### Category listings
![Category](screenshots/products-2.png)

---

## ✨ Future Features

- ⭐ Premium Listings
- 🧾 Transaction History
- 💳 Payflex, Pay just now
- 🛒 Favorites/Wishlist
- 📧 Email Verification
- ⭐ Seller Ratings and Reviews

---

## 🙌 Credits

Designed and built with ❤️ by Yandisa Gaju — Aspiring Software Developer

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 🐳 Docker Setup

Prefer containers? You can run HustleHub with Docker:

1. **Build the image:**
   ```bash
   docker build -t hustlehub .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8000:8000 hustlehub
   ```

3. Open your browser:  
   [http://localhost:8000](http://localhost:8000)

> ✅ Make sure `requirements.txt` includes `Pillow`, and your `.env` file is excluded via `.gitignore`.

---

## 📘 Developer Documentation

This project includes Sphinx-generated developer documentation.

To view it locally:

1. Open the file:
   ```
   docs/build/html/index.html
   ```

2. Or serve the docs locally:
   ```bash
   cd docs/build/html
   python -m http.server
   ```

Then visit:  
[http://localhost:8000](http://localhost:8000)
