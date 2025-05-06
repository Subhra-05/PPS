s=input("")
m_s=""
for char in s:
	if char.isalnum() or char.isspace():
		m_s+=char
print(m_s)
