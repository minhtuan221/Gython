'''
generics classes with common base.
'''
class A:
	def __init__(self, x:int):
		int self.x = x

	def method1(self) -> int:
		return self.x

class B(A):

	def method1(self) ->int:
		return self.x * 2

class C(A):

	def method1(self) ->int:
		return self.x + 100


def my_generic( g:A ) ->int:
	return g.method1()

def main():
	a = A( 100 )
	b = B( 100 )
	c = C( 100 )

	x = my_generic( a )
	print( x )

	y = my_generic( b )
	print( y )

	z = my_generic( c )
	print( z )
