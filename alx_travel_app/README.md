# 🛫 ALX Travel App 0x00  

This project is part of the **ALX Backend Specialization**.  
It extends the travel booking application by introducing **database models**, **API serializers**, and a **custom seeding command**.  

---

## 📌 Features  

- **Database Models**  
  - `Listing` – Represents properties available for booking.  
  - `Booking` – Represents user bookings linked to a listing.  
  - `Review` – Represents customer feedback for a booking.  

- **Serializers**  
  - Convert Django models (`Listing`, `Booking`) into JSON for API responses using Django REST Framework (DRF).  

- **Database Seeding**  
  - A custom management command `seed` to populate the database with sample data for development and testing.  

---

## 🚀 Getting Started  

### 1️⃣ Clone the Repository  
```  
git clone https://github.com/<your-username>/alx_travel_app_0x00.git  
cd alx_travel_app_0x00  
```  

### 2️⃣ Install Dependencies  
Make sure you have **Python 3.x** and **pip** installed. Then run:  
```  
pip install -r requirements.txt  
```  

### 3️⃣ Apply Migrations  
```  
python manage.py migrate  
```  

### 4️⃣ Run Development Server  
```  
python manage.py runserver  
```  

Visit: <http://127.0.0.1:8000>  

---

## 🌱 Seeding the Database  

Run the custom seed command to insert sample listings:  
```  
python manage.py seed  
```  

---

## 📂 Project Structure  

```  
alx_travel_app_0x00/  
 ├── README.md  
 ├── manage.py  
 ├── alx_travel_app/  
 │    ├── settings.py  
 │    └── urls.py  
 └── listings/  
      ├── models.py  
      ├── serializers.py  
      └── management/  
           └── commands/  
                ├── __init__.py  
                └── seed.py  
```  

---

## ✨ Learning Objectives  

- Model relational data in Django  
- Serialize data with DRF  
- Automate database population with seeding  

---
