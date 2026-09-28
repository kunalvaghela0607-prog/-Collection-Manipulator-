print("Welcome to the Student Data Organizer!") 
student_list = [] 
while True : 
    print("\nSelect an option:") 
    print("1. Add Student") 
    print("2. Display All Students") 
    print("3. Update Student Information") 
    print("4. Delete Student") 
    print("5. Display Subjects Offered") 
    print("6. Exit") 
    print() 
    a = int(input("Enter your choice: ")) 
    print() 
    
    if a ==1: 
      print("Enter Student details:") 
      std_id=int(input(" Student_ID : ")) 
      name=input(" Name : ") 
      age=int(input(" age : ")) 
      grade=input(" Grade : ") 
      dob=input(" Date of Birth (YYYY-MM-DD) : ")	 
      subject_list=input("Subject : ").split(",") 
 
      subject = set() 
 
       
      for sub in subject_list: 
          subject.add(sub.strip()) 
      print() 
 
      fix=(std_id,dob) #tuple 
 
      student = { 
            "name": name, 
            "age": age, 
            "grade": grade , 
            "subjects": subject,  
            "infom": fix 
        } 
      student_list.append (student) 
 
 
      print() 
      print("Student added successfully!") 
 
 
    elif a == 2: 
        print(" --- Display All Student --- ") 
 
        for student in student_list: 
            print( 
                f"Student ID: {student['infom'][0]} | " 
                f"Name: {student['name']} | " 
                f"Age: {student['age']} | " 
                f"Grade: {student['grade']} | " 
                f"Subject: {student['subjects']}" 
            ) 
 
 
    elif a == 3: 
        print(" --- Update Student Information --- ") 
 
        std_id = int(input("Enter student id : ")) 
 
        for student in student_list: 
            print("") 
 
            if student["infom"][0] == std_id: 
                print("Enter new details:") 
 
 
                student["name"] = input("Name: ") 
                student["age"] = int(input("Age: ")) 
                student["grade"] = input("Grade: ") 
            
                subject_input = input("Subjects (comma separated): ").split(",")
                subject_set = set()
                for sub in subject_input:
                    subject_set.add(sub.strip())
                student["subjects"] = subject_set
 
                print() 
                print("Student information updated successfully!") 
                break 
 
        else: 
            print("student not found") 
 
 
    elif a ==4 : 
       print("--- Delete Student ---")  
       std_id = int(input("Enter your student id : ")) 
       for std in student_list: 
          if std["infom"][0]==std_id: 
             student_list.remove(std) 
             print("Student deleted successfully!") 
             break 
        
       else : 
          print("Id not match") 
      
          
    elif a == 5: 
        
        all_subject = set() 
    
        for student in student_list:  
            
            if "subjects" in student:  
                
                subjects = student["subjects"]
                
                for subj in subjects:  
                    all_subject.add(subj)
        
        print("--- Subjects Offered ---") 
        
        if all_subject:
            for subject in sorted(all_subject):
                print(subject)
        else:
            print("No subjects found")
    
    elif a == 6: 
        print("Exit the programme")  
        print("Thank you for using Programme")  
    else:
        print("Invalid choice. Please try again.")
        break