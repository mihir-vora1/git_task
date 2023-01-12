class Solution:
	# sum of two number
	def sub_two_number(self, a=0, b=0):
		return int(a) - int(b)

if __name__ == '__main__':
	ob = Solution()
	res = ob.sub_two_number(10, 20)
	print(res)