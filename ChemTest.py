#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import random
import os

class choose:
	def __init__(self,question,answer,a,b,c,d=""):
		self.question = question
		self.answer = answer
		self.a = a
		self.b = b
		self.c = c
		self.d = d

class tf:
	def __init__(self, question, answer):
		self.question = question
		self.answer = answer
		

def choose_exersice():
	right = 0;
	wrong = 0;
	for ch in chose:
		os.system('clear')
		print(ch.question+'\n');
		print('A. '+ch.a+'\n'+'B. '+ch.b+'\n'+'C. '+ch.c);
		if ch.d != "":
			print('D. '+ch.d+'\n')
		c = raw_input('请输入答案\n');

		if c.upper() == ch.answer.strip():
			print("回答正确")
			raw_input("按任意键进入下一道题");
			right += 1
		else:
			if c == 'q':
				break;
			else :
				print("回答错误,答案是"+ch.answer)
				raw_input("按任意键进入下一道题");
				wrong += 1
	print("完成选择题练习，一共做了"+str(right+wrong)+"道题，正确"+str(right)+"题，错误"+str(wrong)+"题");

def TrueFalse_exercise():
	right = 0;
	wrong = 0;
	for t in tfq:
		os.system('clear')
		print(t.question);
		c = raw_input('请输入答案(T\\F)')

		if (c.upper() == 'T' and t.answer.strip() == "正确")or(c.upper == 'F' and t.answer.strip() == "错误"):
			print("回答正确")
			raw_input("按任意键进入下一道题");
			right += 1
		else:
			if c=='q':
				break;
			else:
				print("回答错误，答案是"+t.answer)
				raw_input("按任意键进入下一道题");
				wrong+=1;
	print("完成判断题练习，一共做了"+str(right+wrong)+"道题，正确"+str(right)+"题，错误"+str(wrong)+"题");
		


f1 = open("choose.txt",'r')
f2 = open("TrueFalse.txt",'r')

t1 = f1.read()
t2 = f2.read()

u1 = r"\d+、(.*)?（标准答案： (.) ）\s+A\. (.*?)?\s+B\. (.*?)?\s+C\. (.*?)?\s+(D\. (.*))?";

u2 = r"\d+、(.*)?（标准答案： (.*)）";

r1 = re.compile(u1);
r2 = re.compile(u2);

l1 = r1.findall(t1);
l2 = r2.findall(t2);


fo1 = open('choose.out','w');

chose = []

for question,answer,a,b,c,e,d in l1:
	fo1.write(question+'\n('+answer+')\n'+a+'\n'+b+'\n'+c+'\n'+d+'\n');
	ch = choose(question,answer,a,b,c,d);
	chose.append(ch);

random.shuffle(chose);

tfq = []

for question,answer in l2:
	t = tf(question, answer);
	tfq.append(t)

random.shuffle(tfq);

print("欢迎进入化学实验安全考试练习系统，请选择你要进行的练习：\n")
print("1. 选择题练习\n")
print("2. 判断题练习\n")

choose = raw_input('?');

if choose == '1':
	os.system('clear')
	choose_exersice()
else:
	os.system('clear')
	TrueFalse_exercise()

