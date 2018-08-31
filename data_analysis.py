
#Title: average()
#Description: computes average of set of numbers
def average(numbers):
	average = 0
	count = 0
	for number in numbers:
		count += 1
		average += number
	average = average/count
	
	return average

'''
def stddev(numbers):
	average = average(numbers)
	stddev = 0
	count = 0
	for x in numbers:
		stddev = stddev += (x-average)**2
		count += 1

	stddev = stddev/count

	return stddev
'''
def main():
	print('Welcome to the data analysis calculator')

	command = ''
	while (command != 'q'):
		command = input('What are you trying to do? Select number of option.\n1. Sum\n2. Difference\n3. Average\n4. Standard Deviation\n')
		if command == '1':
			print('Sum - this will return the absolute value of the sum of the numbers.')
			Sum =  0
			num_of_numbers = int(input('How many numbers do you want to add?\t'))

			while num_of_numbers > 0:
				num_to_add = int(input('Number to add: '))
				Sum += num_to_add
				num_of_numbers -= 1
			print('Total = ' + str(Sum) + '\n')
			#return Sum




		if command == '2':
			print('Difference - this will return the absolute value of the difference between the two numbers.')
			first_number = int(input('What is the first number?\t'))
			second_number = int(input('What is the second number?\t'))
			Difference = first_number - second_number
			if(Difference < 0):
				Difference *= -1
			print('Difference = ' + str(Difference) + '\n')
			#return Difference

		if command == '3':
			print('Average - this will return the average of the numbers.')
			Sum = 0
			Average = 0
			num_of_numbers = int(input('How many numbers do you want to take the average of?\t'))
			total_numbers = num_of_numbers

			while num_of_numbers > 0:
				num_to_add = int(input('Number to add: '))
				Sum += num_to_add
				num_of_numbers -= 1
			Average = Sum/total_numbers
			print('Average = ' + str(Average) + '\n')
			#return Average


		if command == '4':
			print('Standard Deviaion - this will return the standard deviation of the numbers.')

			#1. calculate average
			Sum = 0
			Average = 0
			num_of_numbers = int(input('How many numbers do you want to take the standard deviation of?\t'))
			total_numbers = num_of_numbers

			while num_of_numbers > 0:
				num_to_add = int(input('Number to add: '))
				Sum += num_to_add
				num_of_numbers -= 1
			Average = Sum/total_numbers


			stddev = 0
			count = 0
			while num_of_numbers > 0:
				stddev = stddev + (x-Average)**2
				count += 1
				num_of_numbers -= 1
				count += 1
				
			stddev = stddev/count
			

		if command == 'q':
				print('Thank you for using the data analysis calculator.')

		else:
			print('Unknown command, please try again')
			#command = 'q'
			#test_numbers = [1,5,2]
			#avg = average(test_numbers)
			#print(avg)


main()