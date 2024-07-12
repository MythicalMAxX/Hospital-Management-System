# importing required libraries
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog


# Class to manage medical history entries for patients
class MedicalHistory:
    def __init__(self):
        self.entries = []

    def add_entry(self, patient_id, history_details, date):
        self.entries.append({'patient_id': patient_id, 'history_details': history_details, 'date': date})

    def get_history(self, patient_id):
        return [entry for entry in self.entries if entry['patient_id'] == patient_id]

    def delete_entry(self, index):
        del self.entries[index]

    def edit_entry(self, index, history_details, date):
        self.entries[index]['history_details'] = history_details
        self.entries[index]['date'] = date


# Class to manage appointments for patients with doctors
class Appointment:
    def __init__(self):
        self.appointments = []

    def schedule_appointment(self, appointment_id, patient_id, doctor_id, date, time, reason):
        self.appointments.append(
            {'appointment_id': appointment_id, 'patient_id': patient_id, 'doctor_id': doctor_id, 'date': date,
             'time': time, 'reason': reason})

    def get_appointments(self, patient_id):
        return [appointment for appointment in self.appointments if appointment['patient_id'] == patient_id]

    def delete_appointment(self, index):
        del self.appointments[index]

    def edit_appointment(self, index, date, time, reason):
        self.appointments[index]['date'] = date
        self.appointments[index]['time'] = time
        self.appointments[index]['reason'] = reason


# Class to manage billing information for patients
class Bills:
    def __init__(self):
        self.bills = []

    def generate_bill(self, bill_id, patient_id, amount, date, status):
        self.bills.append(
            {'bill_id': bill_id, 'patient_id': patient_id, 'amount': amount, 'date': date, 'status': status})

    def get_bills(self, patient_id):
        return [bill for bill in self.bills if bill['patient_id'] == patient_id]

    def delete_bill(self, index):
        del self.bills[index]

    def edit_bill(self, index, amount, date, status):
        self.bills[index]['amount'] = amount
        self.bills[index]['date'] = date
        self.bills[index]['status'] = status


# Class to manage prescriptions for patients
class Prescription:
    def __init__(self):
        self.prescriptions = []

    def create_prescription(self, prescription_id, patient_id, doctor_id, medication_details, date):
        self.prescriptions.append({'prescription_id': prescription_id, 'patient_id': patient_id, 'doctor_id': doctor_id,
                                   'medication_details': medication_details, 'date': date})

    def get_prescriptions(self, patient_id):
        return [prescription for prescription in self.prescriptions if prescription['patient_id'] == patient_id]

    def delete_prescription(self, index):
        del self.prescriptions[index]

    def edit_prescription(self, index, medication_details, date):
        self.prescriptions[index]['medication_details'] = medication_details
        self.prescriptions[index]['date'] = date


# Class to manage lab reports for patients
class LabReports:
    def __init__(self):
        self.reports = []

    def add_report(self, report_id, patient_id, test_details, date, result):
        self.reports.append(
            {'report_id': report_id, 'patient_id': patient_id, 'test_details': test_details, 'date': date,
             'result': result})

    def get_reports(self, patient_id):
        return [report for report in self.reports if report['patient_id'] == patient_id]

    def delete_report(self, index):
        del self.reports[index]

    def edit_report(self, index, test_details, date, result):
        self.reports[index]['test_details'] = test_details
        self.reports[index]['date'] = date
        self.reports[index]['result'] = result


# Class to manage administrators in the system
class Administrator:
    def __init__(self):
        self.admins = []

    def add_admin(self, admin_id, name, contact_info):
        self.admins.append({'admin_id': admin_id, 'name': name, 'contact_info': contact_info})

    def get_admin_info(self, admin_id):
        for admin in self.admins:
            if admin['admin_id'] == admin_id:
                return admin
        return None

    def get_all_admins(self):
        return self.admins

    def delete_admin(self, index):
        del self.admins[index]

    def edit_admin(self, index, name, contact_info):
        self.admins[index]['name'] = name
        self.admins[index]['contact_info'] = contact_info


# Class to manage doctors in the system
class Doctor:
    def __init__(self):
        self.doctors = []

    def add_doctor(self, doctor_id, name, specialization, contact_info):
        self.doctors.append(
            {'doctor_id': doctor_id, 'name': name, 'specialization': specialization, 'contact_info': contact_info})

    def get_doctor_info(self, doctor_id):
        for doctor in self.doctors:
            if doctor['doctor_id'] == doctor_id:
                return doctor
        return None

    def get_all_doctors(self):
        return self.doctors

    def delete_doctor(self, index):
        del self.doctors[index]

    def edit_doctor(self, index, name, specialization, contact_info):
        self.doctors[index]['name'] = name
        self.doctors[index]['specialization'] = specialization
        self.doctors[index]['contact_info'] = contact_info


# Class to manage patients in the system
class Patient:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient_id, name, contact_info, age, gender):
        self.patients.append(
            {'patient_id': patient_id, 'name': name, 'contact_info': contact_info, 'age': age, 'gender': gender})

    def get_patient_info(self, patient_id):
        for patient in self.patients:
            if patient['patient_id'] == patient_id:
                return patient
        return None

    def get_all_patients(self):
        return self.patients

    def delete_patient(self, index):
        del self.patients[index]

    def edit_patient(self, index, name, contact_info, age, gender):
        self.patients[index]['name'] = name
        self.patients[index]['contact_info'] = contact_info
        self.patients[index]['age'] = age
        self.patients[index]['gender'] = gender


# Tkinter interface for the Healthcare Management System
class HealthcareSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Healthcare Management System")

        # Initialize data management classes
        self.medical_history = MedicalHistory()
        self.appointments = Appointment()
        self.bills = Bills()
        self.prescriptions = Prescription()
        self.lab_reports = LabReports()
        self.administrator = Administrator()
        self.doctors = Doctor()
        self.patients = Patient()

        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.create_widgets()

    def create_widgets(self):
        self.tabs = ttk.Notebook(self.main_frame)

        # Create tabs for each section
        self.tab_medical_history = ttk.Frame(self.tabs)
        self.tab_appointments = ttk.Frame(self.tabs)
        self.tab_bills = ttk.Frame(self.tabs)
        self.tab_prescriptions = ttk.Frame(self.tabs)
        self.tab_lab_reports = ttk.Frame(self.tabs)
        self.tab_administrator = ttk.Frame(self.tabs)
        self.tab_doctors = ttk.Frame(self.tabs)
        self.tab_patients = ttk.Frame(self.tabs)

        self.tabs.add(self.tab_medical_history, text="Medical History")
        self.tabs.add(self.tab_appointments, text="Appointments")
        self.tabs.add(self.tab_bills, text="Bills")
        self.tabs.add(self.tab_prescriptions, text="Prescriptions")
        self.tabs.add(self.tab_lab_reports, text="Lab Reports")
        self.tabs.add(self.tab_administrator, text="Administrator")
        self.tabs.add(self.tab_doctors, text="Doctors")
        self.tabs.add(self.tab_patients, text="Patients")

        self.tabs.pack(fill=tk.BOTH, expand=True)

        self.create_medical_history_tab()
        self.create_appointments_tab()
        self.create_bills_tab()
        self.create_prescriptions_tab()
        self.create_lab_reports_tab()
        self.create_administrator_tab()
        self.create_doctors_tab()
        self.create_patients_tab()

    # Create widgets for each tab
    def create_medical_history_tab(self):
        ttk.Label(self.tab_medical_history, text="Patient ID").grid(column=0, row=0, padx=10, pady=10)
        self.medical_history_patient_id = ttk.Entry(self.tab_medical_history)
        self.medical_history_patient_id.grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(self.tab_medical_history, text="History Details").grid(column=0, row=1, padx=10, pady=10)
        self.medical_history_details = ttk.Entry(self.tab_medical_history)
        self.medical_history_details.grid(column=1, row=1, padx=10, pady=10)

        ttk.Label(self.tab_medical_history, text="Date").grid(column=0, row=2, padx=10, pady=10)
        self.medical_history_date = ttk.Entry(self.tab_medical_history)
        self.medical_history_date.grid(column=1, row=2, padx=10, pady=10)

        ttk.Button(self.tab_medical_history, text="Add Entry", command=self.add_medical_history_entry).grid(column=0,
                                                                                                            row=3,
                                                                                                            padx=10,
                                                                                                            pady=10)
        ttk.Button(self.tab_medical_history, text="View History", command=self.view_medical_history).grid(column=1,
                                                                                                          row=3,
                                                                                                          padx=10,
                                                                                                          pady=10)

    def create_appointments_tab(self):
        ttk.Label(self.tab_appointments, text="Appointment ID").grid(column=0, row=0, padx=10, pady=10)
        self.appointment_id = ttk.Entry(self.tab_appointments)
        self.appointment_id.grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(self.tab_appointments, text="Patient ID").grid(column=0, row=1, padx=10, pady=10)
        self.appointment_patient_id = ttk.Entry(self.tab_appointments)
        self.appointment_patient_id.grid(column=1, row=1, padx=10, pady=10)

        ttk.Label(self.tab_appointments, text="Doctor ID").grid(column=0, row=2, padx=10, pady=10)
        self.appointment_doctor_id = ttk.Entry(self.tab_appointments)
        self.appointment_doctor_id.grid(column=1, row=2, padx=10, pady=10)

        ttk.Label(self.tab_appointments, text="Date").grid(column=0, row=3, padx=10, pady=10)
        self.appointment_date = ttk.Entry(self.tab_appointments)
        self.appointment_date.grid(column=1, row=3, padx=10, pady=10)

        ttk.Label(self.tab_appointments, text="Time").grid(column=0, row=4, padx=10, pady=10)
        self.appointment_time = ttk.Entry(self.tab_appointments)
        self.appointment_time.grid(column=1, row=4, padx=10, pady=10)

        ttk.Label(self.tab_appointments, text="Reason").grid(column=0, row=5, padx=10, pady=10)
        self.appointment_reason = ttk.Entry(self.tab_appointments)
        self.appointment_reason.grid(column=1, row=5, padx=10, pady=10)

        ttk.Button(self.tab_appointments, text="Schedule Appointment", command=self.schedule_appointment).grid(column=0,
                                                                                                               row=6,
                                                                                                               padx=10,
                                                                                                               pady=10)
        ttk.Button(self.tab_appointments, text="View Appointments", command=self.view_appointments).grid(column=1,
                                                                                                         row=6, padx=10,
                                                                                                         pady=10)

    def create_bills_tab(self):
        ttk.Label(self.tab_bills, text="Bill ID").grid(column=0, row=0, padx=10, pady=10)
        self.bill_id = ttk.Entry(self.tab_bills)
        self.bill_id.grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(self.tab_bills, text="Patient ID").grid(column=0, row=1, padx=10, pady=10)
        self.bill_patient_id = ttk.Entry(self.tab_bills)
        self.bill_patient_id.grid(column=1, row=1, padx=10, pady=10)

        ttk.Label(self.tab_bills, text="Amount").grid(column=0, row=2, padx=10, pady=10)
        self.bill_amount = ttk.Entry(self.tab_bills)
        self.bill_amount.grid(column=1, row=2, padx=10, pady=10)

        ttk.Label(self.tab_bills, text="Date").grid(column=0, row=3, padx=10, pady=10)
        self.bill_date = ttk.Entry(self.tab_bills)
        self.bill_date.grid(column=1, row=3, padx=10, pady=10)

        ttk.Label(self.tab_bills, text="Status").grid(column=0, row=4, padx=10, pady=10)
        self.bill_status = ttk.Entry(self.tab_bills)
        self.bill_status.grid(column=1, row=4, padx=10, pady=10)

        ttk.Button(self.tab_bills, text="Generate Bill", command=self.generate_bill).grid(column=0, row=5, padx=10,
                                                                                          pady=10)
        ttk.Button(self.tab_bills, text="View Bills", command=self.view_bills).grid(column=1, row=5, padx=10, pady=10)

    def create_prescriptions_tab(self):
        ttk.Label(self.tab_prescriptions, text="Prescription ID").grid(column=0, row=0, padx=10, pady=10)
        self.prescription_id = ttk.Entry(self.tab_prescriptions)
        self.prescription_id.grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(self.tab_prescriptions, text="Patient ID").grid(column=0, row=1, padx=10, pady=10)
        self.prescription_patient_id = ttk.Entry(self.tab_prescriptions)
        self.prescription_patient_id.grid(column=1, row=1, padx=10, pady=10)

        ttk.Label(self.tab_prescriptions, text="Doctor ID").grid(column=0, row=2, padx=10, pady=10)
        self.prescription_doctor_id = ttk.Entry(self.tab_prescriptions)
        self.prescription_doctor_id.grid(column=1, row=2, padx=10, pady=10)

        ttk.Label(self.tab_prescriptions, text="Medication Details").grid(column=0, row=3, padx=10, pady=10)
        self.prescription_medication_details = ttk.Entry(self.tab_prescriptions)
        self.prescription_medication_details.grid(column=1, row=3, padx=10, pady=10)

        ttk.Label(self.tab_prescriptions, text="Date").grid(column=0, row=4, padx=10, pady=10)
        self.prescription_date = ttk.Entry(self.tab_prescriptions)
        self.prescription_date.grid(column=1, row=4, padx=10, pady=10)

        ttk.Button(self.tab_prescriptions, text="Create Prescription", command=self.create_prescription).grid(column=0,
                                                                                                              row=5,
                                                                                                              padx=10,
                                                                                                              pady=10)
        ttk.Button(self.tab_prescriptions, text="View Prescriptions", command=self.view_prescriptions).grid(column=1,
                                                                                                            row=5,
                                                                                                            padx=10,
                                                                                                            pady=10)

    def create_lab_reports_tab(self):
        ttk.Label(self.tab_lab_reports, text="Report ID").grid(column=0, row=0, padx=10, pady=10)
        self.report_id = ttk.Entry(self.tab_lab_reports)
        self.report_id.grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(self.tab_lab_reports, text="Patient ID").grid(column=0, row=1, padx=10, pady=10)
        self.report_patient_id = ttk.Entry(self.tab_lab_reports)
        self.report_patient_id.grid(column=1, row=1, padx=10, pady=10)

        ttk.Label(self.tab_lab_reports, text="Test Details").grid(column=0, row=2, padx=10, pady=10)
        self.report_test_details = ttk.Entry(self.tab_lab_reports)
        self.report_test_details.grid(column=1, row=2, padx=10, pady=10)

        ttk.Label(self.tab_lab_reports, text="Date").grid(column=0, row=3, padx=10, pady=10)
        self.report_date = ttk.Entry(self.tab_lab_reports)
        self.report_date.grid(column=1, row=3, padx=10, pady=10)

        ttk.Label(self.tab_lab_reports, text="Result").grid(column=0, row=4, padx=10, pady=10)
        self.report_result = ttk.Entry(self.tab_lab_reports)
        self.report_result.grid(column=1, row=4, padx=10, pady=10)

        ttk.Button(self.tab_lab_reports, text="Add Report", command=self.add_report).grid(column=0, row=5, padx=10,
                                                                                          pady=10)
        ttk.Button(self.tab_lab_reports, text="View Reports", command=self.view_reports).grid(column=1, row=5, padx=10,
                                                                                              pady=10)

    def create_administrator_tab(self):
        ttk.Label(self.tab_administrator, text="Admin ID").grid(column=0, row=0, padx=10, pady=10)
        self.admin_id = ttk.Entry(self.tab_administrator)
        self.admin_id.grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(self.tab_administrator, text="Name").grid(column=0, row=1, padx=10, pady=10)
        self.admin_name = ttk.Entry(self.tab_administrator)
        self.admin_name.grid(column=1, row=1, padx=10, pady=10)

        ttk.Label(self.tab_administrator, text="Contact Info").grid(column=0, row=2, padx=10, pady=10)
        self.admin_contact_info = ttk.Entry(self.tab_administrator)
        self.admin_contact_info.grid(column=1, row=2, padx=10, pady=10)

        ttk.Button(self.tab_administrator, text="Add Admin", command=self.add_admin).grid(column=0, row=3, padx=10,
                                                                                          pady=10)
        ttk.Button(self.tab_administrator, text="View Admin Info", command=self.view_admin_info).grid(column=1, row=3,
                                                                                                      padx=10, pady=10)

    def create_doctors_tab(self):
        ttk.Label(self.tab_doctors, text="Doctor ID").grid(column=0, row=0, padx=10, pady=10)
        self.doctor_id = ttk.Entry(self.tab_doctors)
        self.doctor_id.grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(self.tab_doctors, text="Name").grid(column=0, row=1, padx=10, pady=10)
        self.doctor_name = ttk.Entry(self.tab_doctors)
        self.doctor_name.grid(column=1, row=1, padx=10, pady=10)

        ttk.Label(self.tab_doctors, text="Specialization").grid(column=0, row=2, padx=10, pady=10)
        self.doctor_specialization = ttk.Entry(self.tab_doctors)
        self.doctor_specialization.grid(column=1, row=2, padx=10, pady=10)

        ttk.Label(self.tab_doctors, text="Contact Info").grid(column=0, row=3, padx=10, pady=10)
        self.doctor_contact_info = ttk.Entry(self.tab_doctors)
        self.doctor_contact_info.grid(column=1, row=3, padx=10, pady=10)

        ttk.Button(self.tab_doctors, text="Add Doctor", command=self.add_doctor).grid(column=0, row=4, padx=10, pady=10)
        ttk.Button(self.tab_doctors, text="View Doctor Info", command=self.view_doctor_info).grid(column=1, row=4,
                                                                                                  padx=10, pady=10)

    def create_patients_tab(self):
        ttk.Label(self.tab_patients, text="Patient ID").grid(column=0, row=0, padx=10, pady=10)
        self.patient_id = ttk.Entry(self.tab_patients)
        self.patient_id.grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(self.tab_patients, text="Name").grid(column=0, row=1, padx=10, pady=10)
        self.patient_name = ttk.Entry(self.tab_patients)
        self.patient_name.grid(column=1, row=1, padx=10, pady=10)

        ttk.Label(self.tab_patients, text="Contact Info").grid(column=0, row=2, padx=10, pady=10)
        self.patient_contact_info = ttk.Entry(self.tab_patients)
        self.patient_contact_info.grid(column=1, row=2, padx=10, pady=10)

        ttk.Label(self.tab_patients, text="Age").grid(column=0, row=3, padx=10, pady=10)
        self.patient_age = ttk.Entry(self.tab_patients)
        self.patient_age.grid(column=1, row=3, padx=10, pady=10)

        ttk.Label(self.tab_patients, text="Gender").grid(column=0, row=4, padx=10, pady=10)
        self.patient_gender = ttk.Entry(self.tab_patients)
        self.patient_gender.grid(column=1, row=4, padx=10, pady=10)

        ttk.Button(self.tab_patients, text="Add Patient", command=self.add_patient).grid(column=0, row=5, padx=10,
                                                                                         pady=10)
        ttk.Button(self.tab_patients, text="View Patient Info", command=self.view_patient_info).grid(column=1, row=5,
                                                                                                     padx=10, pady=10)

    # Format data for display
    def format_data(self, data):
        return "\n".join([f"{key}: {value}" for key, value in data.items()])

    # Event handlers for each operation
    def add_medical_history_entry(self):
        try:
            patient_id = self.medical_history_patient_id.get()
            history_details = self.medical_history_details.get()
            date = self.medical_history_date.get()
            self.medical_history.add_entry(patient_id, history_details, date)
            messagebox.showinfo("Success", "Medical history entry added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add medical history entry: {e}")

    def view_medical_history(self):
        try:
            patient_id = self.medical_history_patient_id.get()
            history = self.medical_history.get_history(patient_id)
            self.open_data_window(history, "Medical History", self.medical_history.delete_entry,
                                  self.medical_history.edit_entry)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve medical history: {e}")

    def schedule_appointment(self):
        try:
            appointment_id = self.appointment_id.get()
            patient_id = self.appointment_patient_id.get()
            doctor_id = self.appointment_doctor_id.get()
            date = self.appointment_date.get()
            time = self.appointment_time.get()
            reason = self.appointment_reason.get()
            self.appointments.schedule_appointment(appointment_id, patient_id, doctor_id, date, time, reason)
            messagebox.showinfo("Success", "Appointment scheduled successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to schedule appointment: {e}")

    def view_appointments(self):
        try:
            patient_id = self.appointment_patient_id.get()
            appointments = self.appointments.get_appointments(patient_id)
            self.open_data_window(appointments, "Appointments", self.appointments.delete_appointment,
                                  self.appointments.edit_appointment)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve appointments: {e}")

    def generate_bill(self):
        try:
            bill_id = self.bill_id.get()
            patient_id = self.bill_patient_id.get()
            amount = self.bill_amount.get()
            date = self.bill_date.get()
            status = self.bill_status.get()
            self.bills.generate_bill(bill_id, patient_id, amount, date, status)
            messagebox.showinfo("Success", "Bill generated successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate bill: {e}")

    def view_bills(self):
        try:
            patient_id = self.bill_patient_id.get()
            bills = self.bills.get_bills(patient_id)
            self.open_data_window(bills, "Bills", self.bills.delete_bill, self.bills.edit_bill)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve bills: {e}")

    def create_prescription(self):
        try:
            prescription_id = self.prescription_id.get()
            patient_id = self.prescription_patient_id.get()
            doctor_id = self.prescription_doctor_id.get()
            medication_details = self.prescription_medication_details.get()
            date = self.prescription_date.get()
            self.prescriptions.create_prescription(prescription_id, patient_id, doctor_id, medication_details, date)
            messagebox.showinfo("Success", "Prescription created successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create prescription: {e}")

    def view_prescriptions(self):
        try:
            patient_id = self.prescription_patient_id.get()
            prescriptions = self.prescriptions.get_prescriptions(patient_id)
            self.open_data_window(prescriptions, "Prescriptions", self.prescriptions.delete_prescription,
                                  self.prescriptions.edit_prescription)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve prescriptions: {e}")

    def add_report(self):
        try:
            report_id = self.report_id.get()
            patient_id = self.report_patient_id.get()
            test_details = self.report_test_details.get()
            date = self.report_date.get()
            result = self.report_result.get()
            self.lab_reports.add_report(report_id, patient_id, test_details, date, result)
            messagebox.showinfo("Success", "Lab report added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add lab report: {e}")

    # View lab reports for a patient
    def view_reports(self):
        try:
            patient_id = self.report_patient_id.get()
            reports = self.lab_reports.get_reports(patient_id)
            self.open_data_window(reports, "Lab Reports", self.lab_reports.delete_report, self.lab_reports.edit_report)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve lab reports: {e}")

    # Add an administrator to the system
    def add_admin(self):
        try:
            admin_id = self.admin_id.get()
            name = self.admin_name.get()
            contact_info = self.admin_contact_info.get()
            self.administrator.add_admin(admin_id, name, contact_info)
            messagebox.showinfo("Success", "Administrator added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add administrator: {e}")

    def view_admin_info(self):
        try:
            admins = self.administrator.get_all_admins()
            self.open_data_window(admins, "Administrator Info", self.administrator.delete_admin, self.administrator.edit_admin)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve administrator info: {e}")

    def add_doctor(self):
        try:
            doctor_id = self.doctor_id.get()
            name = self.doctor_name.get()
            specialization = self.doctor_specialization.get()
            contact_info = self.doctor_contact_info.get()
            self.doctors.add_doctor(doctor_id, name, specialization, contact_info)
            messagebox.showinfo("Success", "Doctor added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add doctor: {e}")

    def view_doctor_info(self):
        try:
            doctors = self.doctors.get_all_doctors()
            self.open_data_window(doctors, "Doctor Info", self.doctors.delete_doctor, self.doctors.edit_doctor)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve doctor info: {e}")

    def add_patient(self):
        try:
            patient_id = self.patient_id.get()
            name = self.patient_name.get()
            contact_info = self.patient_contact_info.get()
            age = self.patient_age.get()
            gender = self.patient_gender.get()
            self.patients.add_patient(patient_id, name, contact_info, age, gender)
            messagebox.showinfo("Success", "Patient added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add patient: {e}")

    def view_patient_info(self):
        try:
            patients = self.patients.get_all_patients()
            self.open_data_window(patients, "Patient Info", self.patients.delete_patient, self.patients.edit_patient)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve patient info: {e}")

    # Open a new window to display data
    def open_data_window(self, data, title, delete_callback, edit_callback):
        new_window = tk.Toplevel(self.root)
        new_window.title(title)

        for index, item in enumerate(data):
            frame = tk.Frame(new_window)
            frame.pack(fill=tk.X, padx=10, pady=5)

            item_str = self.format_data(item)
            label = tk.Label(frame, text=item_str, anchor="w")
            label.pack(side=tk.LEFT, fill=tk.X, expand=True)

            delete_button = tk.Button(frame, text="Delete",
                                      command=lambda i=index: self.handle_delete(i, delete_callback, new_window))
            delete_button.pack(side=tk.RIGHT, padx=5)

            edit_button = tk.Button(frame, text="Edit",
                                    command=lambda i=index: self.handle_edit(i, item, edit_callback, new_window))
            edit_button.pack(side=tk.RIGHT, padx=5)

    # Handle delete and edit operations
    def handle_delete(self, index, delete_callback, window):
        try:
            delete_callback(index)
            window.destroy()
            messagebox.showinfo("Success", "Entry deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete entry: {e}")

    # Handle edit operations
    def handle_edit(self, index, item, edit_callback, window):
        try:
            if 'history_details' in item:
                new_details = simpledialog.askstring("Edit Entry", "Enter new history details:",
                                                     initialvalue=item['history_details'])
                new_date = simpledialog.askstring("Edit Entry", "Enter new date:", initialvalue=item['date'])
                if new_details and new_date:
                    edit_callback(index, new_details, new_date)
            elif 'date' in item and 'time' in item:
                new_date = simpledialog.askstring("Edit Appointment", "Enter new date:", initialvalue=item['date'])
                new_time = simpledialog.askstring("Edit Appointment", "Enter new time:", initialvalue=item['time'])
                new_reason = simpledialog.askstring("Edit Appointment", "Enter new reason:", initialvalue=item['reason'])
                if new_date and new_time and new_reason:
                    edit_callback(index, new_date, new_time, new_reason)
            elif 'amount' in item:
                new_amount = simpledialog.askstring("Edit Bill", "Enter new amount:", initialvalue=item['amount'])
                new_date = simpledialog.askstring("Edit Bill", "Enter new date:", initialvalue=item['date'])
                new_status = simpledialog.askstring("Edit Bill", "Enter new status:", initialvalue=item['status'])
                if new_amount and new_date and new_status:
                    edit_callback(index, new_amount, new_date, new_status)
            elif 'medication_details' in item:
                new_details = simpledialog.askstring("Edit Prescription", "Enter new medication details:",
                                                     initialvalue=item['medication_details'])
                new_date = simpledialog.askstring("Edit Prescription", "Enter new date:", initialvalue=item['date'])
                if new_details and new_date:
                    edit_callback(index, new_details, new_date)
            elif 'test_details' in item:
                new_test_details = simpledialog.askstring("Edit Report", "Enter new test details:",
                                                          initialvalue=item['test_details'])
                new_date = simpledialog.askstring("Edit Report", "Enter new date:", initialvalue=item['date'])
                new_result = simpledialog.askstring("Edit Report", "Enter new result:", initialvalue=item['result'])
                if new_test_details and new_date and new_result:
                    edit_callback(index, new_test_details, new_date, new_result)
            elif 'name' in item and 'contact_info' in item:
                new_name = simpledialog.askstring("Edit Admin/Doctor", "Enter new name:", initialvalue=item['name'])
                new_contact_info = simpledialog.askstring("Edit Admin/Doctor", "Enter new contact info:",
                                                          initialvalue=item['contact_info'])
                if 'specialization' in item:
                    new_specialization = simpledialog.askstring("Edit Doctor", "Enter new specialization:",
                                                                initialvalue=item['specialization'])
                    if new_name and new_contact_info and new_specialization:
                        edit_callback(index, new_name, new_specialization, new_contact_info)
                elif new_name and new_contact_info:
                    edit_callback(index, new_name, new_contact_info)
            else:
                new_name = simpledialog.askstring("Edit Patient", "Enter new name:", initialvalue=item['name'])
                new_contact_info = simpledialog.askstring("Edit Patient", "Enter new contact info:",
                                                          initialvalue=item['contact_info'])
                new_age = simpledialog.askstring("Edit Patient", "Enter new age:", initialvalue=item['age'])
                new_gender = simpledialog.askstring("Edit Patient", "Enter new gender:", initialvalue=item['gender'])
                if new_name and new_contact_info and new_age and new_gender:
                    edit_callback(index, new_name, new_contact_info, new_age, new_gender)

            window.destroy()
            messagebox.showinfo("Success", "Entry edited successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to edit entry: {e}")


# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = HealthcareSystemApp(root)
    root.mainloop()