from random import randint

n = int(input("enter n: "))
if n == 0:
	exit()

journal = {}
descr = {}

for i in range(1, n+1):
	id_descr = 0
	while True:
		id_descr = randint(0, n + 100)
		if not id_descr in descr:
			break

	descr[id_descr] = {
		'height': randint(100, 200),
		'weight': randint(30, 100),
		'name': [chr(randint(65, 90)) for _ in range(0, randint(3, 10))],
		'marks': [str(randint(2, 5)) for __ in range(0, randint(3, 10))]
	}

	journal[i] = id_descr

while True:
	requested_student_number = int(input("enter student number (1-{}) to get information: ".format(n)))

	if requested_student_number in journal:
		stud_descr = descr[journal[requested_student_number]]
		print("name: ", "".join(stud_descr["name"]))
		print("height: ", stud_descr["height"])
		print("weight: ", stud_descr["weight"])
		print("marks: ", ", ".join(stud_descr["marks"]))

		sum = 0

		for mark in stud_descr["marks"]:
			sum += int(mark)

		print("avg: ", sum / len(stud_descr["marks"]))


	# id_descr = random.
	# descr[n] = id_descr
