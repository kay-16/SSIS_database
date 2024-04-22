/*INSERT INTO student (ID_number, student_name, gender, year_lvl, course_code)
VALUES 
("2015-1234", "John Doe", "male", "1st year", "BAH"),
("2016-5678", "Jane Smith", "female", "2nd year", "BSComEng"),
("2017-9012", "Michael Johnson", "male", "3rd year", "BSEE"),
("2018-3456", "Emily Davis", "female", "4th year", "BSCE"),
("2019-7890", "David Brown", "male", "1st year", "BSPsych"),
("2020-2345", "Sarah Wilson", "female", "2nd year", "BSIS"),
("2021-6789", "James Martinez", "male", "3rd year", "BSME"),
("2022-0123", "Olivia Taylor", "female", "4th year", "BAH"),
("2023-4567", "William Anderson", "male", "1st year", "BSPhy"),
("2024-8901", "Sophia Thomas", "female", "2nd year", "BSStats"),
("2025-2345", "Daniel Hernandez", "male", "3rd year", "BSCS"),
("2026-6789", "Emma Garcia", "female", "4th year", "BSIT"),
("2027-0123", "Alexander Rodriguez", "male", "1st year", "BSE"),
("2028-4567", "Ava Martinez", "female", "2nd year", "BSBM"),
("2029-8901", "Noah Hernandez", "male", "3rd year", "BSE"),
("2030-2345", "Isabella Gonzalez", "female", "4th year", "BAH"),
("2031-6789", "Ethan Lopez", "male", "1st year", "BSComEng"),
("2032-0123", "Mia Perez", "female", "2nd year", "BSEE"),
("2033-4567", "Lucas Wilson", "male", "3rd year", "BSCE"),
("2034-8901", "Avery Lee", "female", "4th year", "BSPsych"),
("2035-2345", "Liam Taylor", "male", "1st year", "BSIS"),
("2036-6789", "Harper Johnson", "female", "2nd year", "BSME"),
("2037-0123", "Benjamin Smith", "male", "3rd year", "BAH"),
("2038-4567", "Evelyn Brown", "female", "4th year", "BSPhy"),
("2039-8901", "Mason Jones", "male", "1st year", "BSStats"),
("2040-2345", "Amelia Davis", "female", "2nd year", "BSCS"),
("2041-6789", "Elijah Miller", "male", "3rd year", "BSIT"),
("2042-0123", "Charlotte Wilson", "female", "4th year", "BSE"),
("2043-4567", "Oliver Martinez", "male", "1st year", "BSBM"),
("2044-8901", "Sophia Hernandez", "female", "2nd year", "BSE"),
("2045-2345", "Jacob Gonzalez", "male", "3rd year", "BSN"),
("2046-6789", "Emily Lopez", "female", "4th year", "BSComEng"),
("2047-0123", "Michael Perez", "male", "1st year", "BSEE"),
("2048-4567", "Emma Wilson", "female", "2nd year", "BSCE"),
("2049-8901", "Daniel Lee", "male", "3rd year", "BSPsych"),
("2050-2345", "Ava Taylor", "female", "4th year", "BSIS"),
("2051-6789", "William Johnson", "male", "1st year", "BSME"),
("2052-0123", "Sophia Smith", "female", "2nd year", "BAH"),
("2053-4567", "James Brown", "male", "3rd year", "BSPhy"),
("2054-8901", "Olivia Jones", "female", "4th year", "BSStats"),
("2055-2345", "Logan Davis", "male", "1st year", "BSCS"),
("2056-6789", "Ella Miller", "female", "2nd year", "BSIT"),
("2057-0123", "Jackson Wilson", "male", "3rd year", "BSE"),
("2058-4567", "Madison Martinez", "female", "4th year", "BSBM"),
("2059-8901", "Lucas Hernandez", "male", "1st year", "BSE"),
("2060-2345", "Harper Gonzalez", "female", "2nd year", "BSN"),
("2061-6789", "Ethan Lopez", "male", "3rd year", "BSComEng"),
("2062-0123", "Mia Perez", "female", "4th year", "BSEE"),
("2063-4567", "Lucas Wilson", "male", "1st year", "BSCE"),
("2064-8901", "Avery Lee", "female", "2nd year", "BSPsych"),
("2065-2345", "Liam Taylor", "male", "3rd year", "BSIS"),
("2066-6789", "Harper Johnson", "female", "4th year", "BSME"),
("2067-0123", "Benjamin Smith", "male", "1st year", "BAH"),
("2068-4567", "Evelyn Brown", "female", "2nd year", "BSPhy"),
("2069-8901", "Mason Jones", "male", "3rd year", "BSStats"),
("2070-2345", "Amelia Davis", "female", "4th year", "BSCS"),
("2071-6789", "Elijah Miller", "male", "1st year", "BSIT"),
("2072-0123", "Charlotte Wilson", "female", "2nd year", "BSE"),
("2073-4567", "Oliver Martinez", "male", "3rd year", "BSBM"),
("2074-8901", "Sophia Hernandez", "female", "4th year", "BSE"),
("2075-2345", "Jacob Gonzalez", "male", "1st year", "BSN"),
("2076-6789", "Emily Lopez", "female", "2nd year", "BSComEng"),
("2077-0123", "Michael Perez", "male", "3rd year", "BSEE"),
("2078-4567", "Emma Wilson", "female", "4th year", "BSCE"),
("2079-8901", "Daniel Lee", "male", "1st year", "BSPsych"),
("2080-2345", "Ava Taylor", "female", "2nd year", "BSIS"),
("2081-6789", "William Johnson", "male", "3rd year", "BSME"),
("2082-0123", "Sophia Smith", "female", "4th year", "BAH"),
("2083-4567", "James Brown", "male", "1st year", "BSPhy"),
("2084-8901", "Olivia Jones", "female", "2nd year", "BSStats"),
("2085-2345", "Logan Davis", "male", "3rd year", "BSCS"),
("2086-6789", "Ella Miller", "female", "4th year", "BSIT"),
("2087-0123", "Jackson Wilson", "male", "1st year", "BSE"),
("2088-4567", "Madison Martinez", "female", "2nd year", "BSBM"),
("2089-8901", "Lucas Hernandez", "male", "3rd year", "BSE"),
("2090-2345", "Harper Gonzalez", "female", "4th year", "BSN"),
("2091-6789", "Ethan Lopez", "male", "1st year", "BSComEng"),
("2092-0123", "Mia Perez", "female", "2nd year", "BSEE"),
("2093-4567", "Lucas Wilson", "male", "3rd year", "BSCE"),
("2094-8901", "Avery Lee", "female", "4th year", "BSPsych"),
("2095-2345", "Liam Taylor", "male", "1st year", "BSIS"),
("2096-6789", "Harper Johnson", "female", "2nd year", "BSME"),
("2097-0123", "Benjamin Smith", "male", "3rd year", "BAH"),
("2098-4567", "Evelyn Brown", "female", "4th year", "BSPhy"),
("2099-8901", "Mason Jones", "male", "1st year", "BSStats"),
("2100-2345", "Amelia Davis", "female", "2nd year", "BSCS");*/


#UPDATE student
#SET course_code = NULL
#WHERE ID_number = "2023-1327";
#SELECT * FROM student;

#SET SQL_SAFE_UPDATES = 0;

/*INSERT INTO course (course_code, course_name)
VALUES ("BSN", "Bachelor of Science in Nursing"),
       ("BSComEng", "Bachelor of Science in Computer Engineering"),
       ("BSEE", "Bachelor of Science in Electrical Engineering"),
	   ("BSCE", "Bachelor of Science in Civil Engineering"),
	   ("BSPsych", "Bachelor of Science in Pyschology"),
	   ("BSIS", "Bachelor of Science in Information System"),
	   ("BSME", "Bachelor of Science in Mechanical Engineering"),
	   ("BAH", "Bachelor of Arts in History"),
	   ("BSPhy", "Bachelor of Science in Physics"),
	   ("BSStats", "Bachelor of Science in Statistics"),
	   ("BSCS", "Bachelor of Science in Computer Science"),
	   ("BSIT", "Bachelor of Science in Information Technology"),
	   ("BSA", "Bachelor of Science in Accountancy"),
	   ("BSBM", "Bachelor of Science in Business Management"),
	   ("BSE", "Bachelor of Science in Economics");*/

#ALTER TABLE student
#ADD CONSTRAINT
#PRIMARY KEY(ID_number);

#ALTER TABLE course
#ADD CONSTRAINT
#PRIMARY KEY(course_code);

#ALTER TABLE student
#ADD CONSTRAINT fk_course_code
#FOREIGN KEY(course_code) REFERENCES course(course_code);

#ALTER TABLE student
#MODIFY year_lvl VARCHAR(20) NOT NULL;

#ALTER TABLE student 
#MODIFY COLUMN year_lvl VARCHAR(50);

SELECT * FROM course
#SELECT * FROM student;



