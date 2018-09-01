
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
		command = input('What are you trying to do? Select option.\n1. Sum\n2. Difference\n3. Multiply\n4. Average\n5. Standard Deviation\n6. Greatest Common Factor\n7. Raise to Power\n8. Is Prime?\n9. Least Common Multiple * Under Construction*\n10. \nq. Quit\nEnter option: ')
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
			print('Multiply - this will return the value of the numbers multiplied')
			print('Input numbers to multiply one at a time, followed by the * key')

			total = 1
			num_elements_to_multiply = int(input('Enter number of numbers to multiply: '))
			while num_elements_to_multiply > 0:
				number_to_multiply = int(input('Enter number: '))
				total *= number_to_multiply
				num_elements_to_multiply -= 1
			print(total + '\n')


		if command == '4':
			print('Average - this will return the average of the numbers.')
			Sum = 0
			Average = 0
			num_of_numbers = int(input('How many numbers do you want to take the average of?\t'))
			total_numbers = num_of_numbers

			while num_of_numbers > 0:
				num_to_add = int(input('Number to average: '))
				Sum += num_to_add
				num_of_numbers -= 1
			Average = Sum/total_numbers
			print('Average = ' + str(Average) + '\n')
			#return Average


		if command == '5':
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

		if command == '6':
			print('Greatest Common Factor - this will return the GCF of the numbers.')
			print('Currently this feature works with only two numbers')

			num1 = int(input('What is the first number?'))
			num2 = int(input('What is the second number?'))

			
			if(num1 > num2):
				maxfactor = num2
			else:
				maxfactor = num1
			gcf = 1
			for i in range(1,maxfactor):
				if(num1%i==0 and num2%i==0):
					gcf = i

			print(gcf + '\n')
			#return gcf

		if command == '7':
			print('Raise to power - this will return result of base to power.')
			num1 = int(input('Enter base: '))
			num2 = int(input('Enter power: '))

			result = num1
			while (num2 > 1):
				result *= num1
				num2 -= 1

			if(num2 == 0):
				result = 1
			print(result)

		if command == '8':
			print('Check if a number is prime.')
			number = int(input('Enter test number: '))

			if(number == 1 or number == 2):
				print('Prime')
			#for(int i=2; i<number; i++)
			for i in range(2,number):
				if number % i == 0:
					print('Not prime')
					break
				else:
					print('Prime')
					break
		
		# NOT DONE
		if command == '9':
			print('Find Least Common Multiple')
			num1 = int(input('Enter first number: '))
			num2 = int(input('Enter second number: '))

			if(num1 > num2):
				LCM = num1
			else:
				LCM = num2

			while (num1 % LCM != 0 and num2 % LCM != 0):
				LCM -= 1

			print(LCM)



		if command == 'q':
				print('Thank you for using the data analysis calculator.')

		#else:
			#print('Unknown command, please try again')
			#command = 'q'
			#test_numbers = [1,5,2]
			#avg = average(test_numbers)
			#print(avg)


main()