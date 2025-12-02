# Service Desk Management System (Python)

This project is a **Python console-based service desk management system** designed for technical support or repair shops.  
It allows registering tickets, managing service counters, calculating waiting times, and generating daily reports based on stored records.

All data is saved in a simple text database: `db.txt`.

---

## 🚀 Main Features

### 🔧 Repair Tickets
- Automatic ticket numbering  
- Timestamp for arrival and service  
- Customer name  
- Product and reported issue  
- Initial cost  
- Additional notes  
- Automatic waiting time calculation  
- Stored in `db.txt`

### 📦 Delivery Tickets
- Automatic ticket numbering  
- Timestamp logging  
- Customer name  
- Cost  
- Additional notes  
- Waiting time calculation  
- Stored in `db.txt`

---

## 📊 Management Menu

Accessible with a security code (**2222**).  
Includes:

1. **Tickets served by date**  
2. **Average waiting time per date**  
3. **Counters (balcões) usage per date**  
4. **Total revenue per date**  
5. **Complete ticket database view**  
6. **Exit program**  
7. **Return to main menu**

---

## 📁 File Structure

All records are written to:

db.txt

yaml
Copiar código

Each line contains:

- Ticket type (Repair/Delivery)  
- Ticket number  
- Arrival timestamp  
- Service timestamp  
- Customer name  
- Counter number  
- Cost  
- Notes  
- Waiting time  

---

## 🕒 Operating Hours

The system only works within predefined hours:

- **00:00 to 23:00**

(Easily adjustable in the code.)

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Run the script:

```bash
python main.py
The main menu will appear automatically.

🛠 Technologies Used
Python 3

datetime module

File handling (.txt storage)

Input validation

Console-based user interface

📌 Project Purpose
This project was developed for academic learning, covering:

Functions and modularity

Error handling

Time calculations

File persistence

Console interaction

Simple data analysis

📜 License
Free to use for educational and personal purposes.

