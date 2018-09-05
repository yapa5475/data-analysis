#Data Analysis 					#
#Author: Yash Parekh			#
#Langauge: python 				#
#Run: python3 data_analysis.py  #
#################################
import sys
import fractions
import math
import itertools

def main():
	print('*********************************************')
	print('*  Welcome to the Data Analysis Calculator  *')
	print('*  Number 9: LCM Under Construction  	    *')
	print('*********************************************\n')

	command = ''
	while (command != 'q'):
		prompt = 'What are you trying to do? Select option.\n1. Sum\n2. Difference\n3. Multiply\n4. Average\n5. Standard Deviation\n6. Greatest Common Factor\n7. Raise to Power\n8. Is Prime?\n9. Least Common Multiple * Under Construction*\n10. Smallest Number Divisble by 1 to N\n11. Factorial Digit Sum\n12. Power digit sum\n13. nth Prime\n14. last ten digits of n^n\n15. Largest palindrome product\n16. x digit fibonacci number\n17. Digit fift powers\n18. Lexicographic permutations\n19. Distinct powers\n20. Coin sums\n21. 13 adjacent digits in the 1000 digit number with greatest product\nq. Quit\nEnter option: '
		#command = input('What are you trying to do? Select option.\n1. Sum\n2. Difference\n3. Multiply\n4. Average\n5. Standard Deviation\n6. Greatest Common Factor\n7. Raise to Power\n8. Is Prime?\n9. Least Common Multiple * Under Construction*\n10. Smallest Number Divisble by 1 to N\n11. Factorial Digit Sum\n12. Power digit sum\n13. nth Prime\n14. last ten digits of n^n\n15. Largest palindrome product\n16. x digit fibonacci number\n17. Digit fift powers\n18. Lexicographic permutations\n19. Distinct powers\n20. Coin sums\n21. 13 adjacent digits in the 1000 digit number with greatest product\nq. Quit\nEnter option: ')
		command = input(prompt)
		if command == '1':
			print('\nSum - this will return the absolute value of the sum of the numbers.')
			Sum =  0
			num_of_numbers = int(input('How many numbers do you want to add?\t'))

			while num_of_numbers > 0:
				num_to_add = int(input('Number to add: '))
				Sum += num_to_add
				num_of_numbers -= 1
			print('Total = ' + str(Sum) + '\n')
			#return Sum




		if command == '2':
			print('\nDifference - this will return the absolute value of the difference between the two numbers.')
			first_number = int(input('What is the first number?\t'))
			second_number = int(input('What is the second number?\t'))
			Difference = first_number - second_number
			if(Difference < 0):
				Difference *= -1
			print('Difference = ' + str(Difference) + '\n')
			#return Difference

		if command == '3':
			print('\nMultiply - this will return the value of the numbers multiplied')
			#print('Input numbers to multiply one at a time, followed by the * key')

			total = 1
			num_elements_to_multiply = int(input('Enter number of numbers to multiply: '))
			while num_elements_to_multiply > 0:
				number_to_multiply = int(input('Enter number: '))
				total *= number_to_multiply
				num_elements_to_multiply -= 1
			print('Total = ' + str(total) + '\n')


		if command == '4':
			print('\nAverage - this will return the average of the numbers.')
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
			print('\nStandard Deviaion - this will return the standard deviation of the numbers.')

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
			print('\nGreatest Common Factor - this will return the GCF of the numbers.')
			print('Currently this feature works with only two numbers')

			num1 = int(input('What is the first number?'))
			num2 = int(input('What is the second number?'))

			if(num1 > num2):
				gcf = num2
			else:
				gcf = num1
			while gcf > 1:
				if num1 % gcf == 0 and num2 % gcf == 0:
					break
				gcf -= 1


			print(gcf)
			print('\n')
			#return gcf

		if command == '7':
			print('\nRaise to power - this will return result of base to power.')
			num1 = int(input('Enter base: '))
			num2 = int(input('Enter power: '))
			power = str(num2)

			result = num1
			while (num2 > 1):
				result *= num1
				num2 -= 1

			if(num2 == 0):
				result = 1
			num1 = str(num1)
			num2 = str(num2)
			result = str(result)
			print(num1 + ' raised to ' + power + ' = ' + result)

		if command == '8':
			print('\nCheck if a number is prime.')
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
			print('\nFind Least Common Multiple of two numbers')
			num1 = int(input('Enter first number: '))
			num2 = int(input('Enter second number: '))
			max_poss_LCM = num1 * num2

			if(num1 > num2):
				starting_multiple = num1
			else:
				starting_multiple = num2
			LCM = 1

			for i in range(starting_multiple, max_poss_LCM):
				if(i % num1 == 0 and i % num2 == 0):
					LCM = i
					print(LCM)

		#Smallest multiple: smallest positive number that is evenly divisible by all numbers 1 to N
		if command == '10':
			print('\nFind smallest multiple divisible by 1 to N')
			num = int(input('Enter number: '))
			ans = 1
			for i in range(1, num+1):
				ans = (ans*i)/fractions.gcd(ans, i)
			print(ans)

		#Project euler 20: Factorial digital sum
		#find sum of digits in n!
		if command == '11':
			print('\nFind sum of digits in n!')
			num = int(input('Enter number: '))
			fact_num = math.factorial(num)
			print(str(num)+'! = ' + str(fact_num))

			sum_fact = 0
			str_num = str(num)
			str_fact_num = str(fact_num)
			for i in range(0,len(str_fact_num)):
				num_to_add = int(str_fact_num[i])
				sum_fact += num_to_add

			print('Sum of digits in ' + str_num + '! = ' + str(sum_fact))


		#Project euler 16: Power digit sum - works 
		#Find the sum of digits in n^m
		if command == '12':
			print('\nPower digit sum. Find sum of digits in n^m')
			base = int(input('Enter base: '))
			power = int(input('Enter power: '))
			answer = 1
			for i in range (0,power):
				answer *= base

			print(answer)
			#sum_answer = 0
			str_answer = str(answer)
			sum_answer = 0
			for i in range(0, len(str_answer)):
				num_to_add = int(str_answer[i])
				#print(num_to_add)
				sum_answer += num_to_add

			print('Sum of digits in ' + str(base) + '^' + str(power) + " = " + str(sum_answer))

		# done
		#Project euler 7: Nth prime
		if command == '13':
			print('\nNth prime. Find the prime number at the nth spot')
			n = int(input('Enter index of n: '))
			primeList = [2]
			attempt = 3
			while len(primeList) < n:
				if all(attempt % prime != 0 for prime in primeList):
					primeList.append(attempt)
				attempt += 2
			print(primeList[-1])

			#print(primeList)
					

		# done
		#Project euler 48
		if command == '14':
			#find the last ten digitsof the series 1^1 + 2^2 + 3^3 + 4^4 +... + 1000^1000
			num = int(input('Enter base/power number: '))
			result = 0
			while num > 0:
				result += num**num
				num -= 1
			print(result)

		#done
		#Project euler 4
		if command == '15':
			#largest palindrome product of two 3 digit numbers
			biggest_palindrome = 0

			for i in range(100, 999):
				for j in range(100, 999):
					test = i * j
					if(is_palindrome(test) and test>biggest_palindrome):
						biggest_palindrome = test

			print(biggest_palindrome)
			return biggest_palindrome

		if command == '16':
			print('x digit fibonacci number')
			x = 1000
			index = 0
			n = sys.maxsize
			a = 1
			b = 1

			while(True):
				b = a + b
				a = b - a
				index += 1

				str_b = str(b)
				if len(str_b) >= x:
					print(index)
					#print(str_b)
					print(len(str_b))
					return index


				

			#print(index)
			#print(index)
			#print(a)
			#print(b)
			#print(x)

		#Project euler 30 - done
		# find the sum of all the numbers that can be written as the sum of fifth powers of their digits
		print('Find the sum of all the numbers that can be written as the sum of fifth powers of their digits\n')
		if command == '17':
			print('Digit fifth powers. Calculating...')
			summ = 0
			i = 10
			while  i< 1000000:
				j = list(str(i))
				digit_sum = 0
				for x in j:
					digit = int(x) ** 5
					digit_sum += digit
				if digit_sum == i:
					summ += i
					#print(i)
				i += 1
			print(summ)

			
		#Project euler 24 - done!
		#find the millionth lexicographic permuations of the digits 0,1,2,3,4,5,6,7,8,9
		if command == '18':
			print('Find the millionth lexicographic permuation of the digits 0-9')
			nums = '0123456789'
			k = 10
			perms = []
			for p in itertools.permutations(nums, k):
				perms.append(p)
			print(perms[999999])

		#Project euler 29 - done!
		#distinct powers. how many distinct rems are in the sequence generated by a^b for 2 <= a <= 100 and 2 <= b <= 100?
		if command == '19':
			print('Distinct terms in the sequence gnereated by a^b (a and b between 2 and 100)')
			distnct_a_b_terms = set()
			for a in range(2, 101):
				for b in range(2, 101):
					result = a ** b
					#print(result)
					distnct_a_b_terms.add(result)
			#print(distnct_a_b_terms)
			print(len(distnct_a_b_terms))

		#Project euler 31 - done
		#coin sums. how many ways can 200 be made using: 1,2,5,10,20,50,100,and 200
		if command == '20':
			print('Ways to make x pounds using the following currency: 1p, 2p, 5p, 10p, 20p, 50p, 1 pound, 2 pounds')
			target = int(input('Enter total pounds to target. For instance, if target is 2 pounds, enter 200: '))
			coins = [1, 2, 5, 10, 20, 50, 100, 200]
			ways = [1] + [0]*target

			for coin in coins:
				for i in range (coin, target+1):
					ways[i] += ways[i - coin]

			print("Ways to make change = ", ways[target])

		#Project euler 8 - done
		#Find 13 adjacent digits that have the greatest product
		if command == '21':
			print('Find the 13 adjacent digits in the number 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450 which have the greatest product. What is the value of this product?')
			s = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
			largstProduct = 0

			for i in range(0, len(s) - 13):
				product = 1

				for j in range(i, i + 13):
					product *= int(s[j: j+1])

				if product > largstProduct:
					largstProduct = product
			print(largstProduct)

		if command == 'q':
			print('Thank you for using the data analysis calculator.')

		else:
			print('\nUnknown command')
			command = 'reset'

		#else:
			#print('Unknown command, please try again')
			#command = 'q'
			#test_numbers = [1,5,2]
			#avg = average(test_numbers)
			#print(avg)


def is_prime(num):
	factor = 2
	while (factor < num):
		if num % factor == 0:
			return False
		factor += 1
		return True

def is_palindrome(num):
	str_num = str(num)
	for x in range(100, 1000):
		for y in range(100, 1000):
			if str_num == str_num[::-1]:
				#print('palindrome')
				return True
			else:
				return False

main()