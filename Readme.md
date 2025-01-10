# Role-Based Access Control System

## **Objective**
This project implements a **Role-Based Access Control (RBAC)** system using **Django Rest Framework (DRF)**. It manages access to various endpoints based on user roles, groups, and types, enforcing access control rules for different user types and roles.

---

## **Features**
1. **User Types**: 
   - Normal User (Basic access).
   - Corporate User (Enhanced access).
2. **Roles**:
   - Admin (Full access).
   - Manager (Limited administrative capabilities).
3. **Groups**:
   - Premium (Access to premium services).
   - Non-Premium (Access to basic services).
4. **Pages**:
   - Flight Booking Page
   - Hotel Booking Page
   - Assistant Flight Booking Page
   - Assistant Hotel Booking Page
5. **Access Control Rules**:
   - **Premium** or **Corporate Users** can access both Assistant Flight and Hotel Booking Pages.
   - **Manager** Role can access both Assistant Pages.
   - **Admin** Role can access all pages.
   - **Normal Users** can only access non-assistant pages (Flight and Hotel Booking Pages).

---

## **Project Setup**

### **1. Clone the Repository**
Clone this repository to your local machine:

git clone https://github.com/ismath-rm/Role-Based-Access-Control-System.git
cd Role-Based-Access-Control-System
