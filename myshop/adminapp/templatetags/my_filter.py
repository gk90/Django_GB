from django import template

register = template.Library()


def experimental(text):
	new_text = ''

	for char in text:
		if text.index(char) != 0 and text.index(char) % 2 == 0:
			char = char.upper()
		new_text = new_text + char

	return new_text


register.filter('experimental', experimental)

