"""Небольшая библиотека для работы с матрицами в Python

Создана Валерием aka GoddesAqua Ефремовым при поддержке 2D-лолей"""

from numbers import Number

def safe_get(list, index):
	if index<len(list):
		return list[index]
	else:
		return None

class Matrix():
	def __init__(self,*matrix):
		"""Создает матрицу из кортежа кортежей чисел одинаковой размерности.
		Каждый кортеж задаёт одну СТРОКУ матрицы"""
		pre_length=None
		for row in matrix:
			if type(row) is tuple and all(isinstance(elem, Number) for elem in row):
				if pre_length and len(row)!=pre_length:
					raise Exception("Длина строк матрицы должна быть одинаковой")
				pre_length=len(row)
			else:
				raise Exception("Переданные аргументы должны являтся кортежами чисел")
		else:
			self.matrix=matrix
			self.r=len(matrix)
			self.c=len(matrix[0]) if len(matrix)>0 else 0

	def __repr__(self):
		result=""
		for row in self.matrix:
			result=result+" ".join(str(elem) for elem in row)+"\n"
		return result[:-1]

	def __getitem__(self,key):
		"""Возвращает объекты матрицы по индексу

		1) Возврат строки по ключу: Matrix[int] либо Matrix[int, 'r']
		2) Возврат столбца по ключу: Matrix[int, 'c']
		3) Возврат значения по ключу: Matrix[row, column]
		4) Возврат среза: (r1,c1):(r2,c2):(step_r, step_c)
		Возможен пропуск атрибутов среза: Matrix[:(,3):(2,)]"""
		if isinstance(key, int):
			return Matrix(self.matrix[key])
		elif isinstance(key, slice):
			try:
				start, stop, step = key.start if key.start else (None, None), key.stop if key.stop else (None, None), key.step if key.step else (None, None)
				result=tuple(tuple(self[i,j] for j in range(safe_get(start, 1) if safe_get(start, 1) else 0, safe_get(stop, 1) if safe_get(stop, 1) else self.c, safe_get(step, 1) if safe_get(step, 1) else 1)) for i in range(safe_get(start, 0) if safe_get(start, 0) else 0, safe_get(stop, 0) if safe_get(stop, 0) else self.r, safe_get(step, 0) if safe_get(step, 0) else 1))
				return Matrix(*result)
			except Exception:
				raise Exception("Срез должен быть образован кортежами целых чисел либо None")
		elif isinstance(key, tuple):
			if len(key)==2:
				if all(isinstance(index, int) for index in key):
					return self.matrix[key[0]][key[1]]
				elif isinstance(key[0], int) and isinstance(key[1], str):
					if key[1]=='r':
						return self[key[0]]
					elif key[1]=='c':
						result=tuple(self[i,key[0]] for i in range(self.r))
						return Matrix(result)
				else:
					raise Exception("Когда ключ является кортежем его элементы должны быть целыми числами")
			else:
				raise Exception("Ключ должен иметь один или два аргумента")
		else:
			raise Exception("Индексы являются целыми числами либо их кортежами либо срезами вида (r1,c1):(r2,c2):(step_r, step_c)")

	def __neg__(self):
		"""Возвращает матрицу со значениями обратными по знаку данной"""
		result=tuple(tuple(-self[i,j] for j in range(self.c)) for i in range(self.r))
		return Matrix(*result)

	def __pos__(self):
		"""Возвращает данную матрицу"""
		return Matrix(*self.matrix)

	def __add__(self,other):
		"""Складывает две матрицы"""
		if isinstance(other, Matrix):
			if self.r==other.r and self.c==other.c:
				result=tuple(tuple(self[i,j]+other[i,j] for j in range(self.c)) for i in range(self.r))
				return Matrix(*result)
			else:
				raise Exception("Матрицы должны иметь одинаковую размерность")
		else:
			raise Exception("Складывать с матрицей можно только матрицу")

	def __sub__(self,other):
		"""Вычитает две матрицы"""
		if isinstance(other, Matrix):
			if self.r==other.r and self.c==other.c:
				result=tuple(tuple(self[i,j]-other[i,j] for j in range(self.c)) for i in range(self.r))
				return Matrix(*result)
			else:
				raise Exception("Матрицы должны иметь одинаковую размерность")
		else:
			raise Exception("Вычитать из матрицы можно только матрицу")

	def __mul__(self,other):
		"""Умножает матрицу на число, либо две матрицы между собой"""
		if isinstance(other, Number):
			result=tuple(tuple(self[i,j]*other for j in range(self.c)) for i in range(self.r))
			return Matrix(*result)
		elif isinstance(other, Matrix):
			if self.c==other.r:
				result=tuple(tuple((sum([self[i,k]*other[k,j] for k in range(self.c)])) for j in range(other.c)) for i in range(self.r))
				return Matrix(*result)  
			else:
				raise Exception("Матрицы должны быть согласованы (Matrix*anotherMatrix -> Matrix.c=anotherMatrix.r)")
		else:
			raise Exception("Умножать матрицу можно только на число или матрицу")

	def __rmul__(self,other):
		"""Умножает объект на матрицу справа (some*Matrix)"""
		if isinstance(other, Number):
			result=tuple(tuple(self[i,j]*other for j in range(self.c)) for i in range(self.r))
			return Matrix(*result)
		else:
			raise Exception("Умножать на матрицу справа можно только на число")

	def transposed(self):
		"""Возвращает транспонированную матрицу"""
		result=tuple(tuple(self[j,i] for j in range(self.r)) for i in range(self.c))
		return Matrix(*result)

	def is_square(self):
		"""Проверяет является ли матрица квадратной"""
		return True if self.c==self.r else False

	def minor(self,r,c):
		"""Возвращает дополнительный минор по индексам элемента"""
		new_r=[i for i in range(self.r)]
		new_r.remove(r)
		new_c=[i for i in range(self.c)]
		new_c.remove(c)
		result=tuple(tuple(self[i,j] for j in new_r) for i in new_c)
		return Matrix(*result)

	def det(self):
		"""Возвращает определитель, если матрица квадратная, либо None"""
		if self.is_square():
			if self.r==0:
				return None
			elif self.r==1:
				return self[0,0]
			elif self.r==2:
				return self[0,0]*self[1,1]-self[0,1]*self[1,0]
			else:
				return sum([(-1)**(1+j)*self[0,j]*self.minor(0,j).det() for j in range(self.r)])
		else:
			return None

	@staticmethod
	def e_matrix(size):
		"""Возвращает единичную матрицу заданного размера"""
		result=tuple(tuple((1 if i==j else 0) for i in range(size)) for j in range(size))
		return Matrix(*result)

	@staticmethod
	def null_matrix(size):
		""""Возвращает нулевую матрицу заданного размера"""
		result=tuple(tuple(0 for i in range(size)) for j in range(size))
		return Matrix(*result)

if __name__ == '__main__':
	test=Matrix((1,2,3),(4,5,6),(7,8,9))
	test2=Matrix((7,8),(9,10),(11,12))
	print(test)
	print(test[1, 'c'])
	print(test.det())