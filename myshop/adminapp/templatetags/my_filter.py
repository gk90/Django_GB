from django import template

register = template.Library()

def experimental(text):
	result = text
	length = len(result)//2
	new_result = result[:length] + '_' + result[length:]

	return new_result

register.filter('experimental', experimental)

