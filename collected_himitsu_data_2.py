"""
###プログラム概要
- 収集したデータより入力データと教師データを作成
"""
#collected himitsu-data by google form 
import os, csv
import random
import himitsu_data_gd
import pandas as pd


#訓練データの作成	
def mk_x_train(all_word_list, word_vec, collected):
	
	#ユーザ毎のデータをまとめた全データ
	x_train = []
	for items in collected:
		#ユーザ毎のデータ
		x_data  = []
		for item in items:
			x_data.append(word_vec[item])
		
		for i in range(4):
			#知っているデータからランダムに5個選択
			x_predata = random.sample(x_data, 3)
			#昇順にソート
			x_predata.sort()
			x_train.append(x_predata)
		
	return x_train
	
	
#教師データの作成
def mk_y_train(all_word_list, collected):
	y_train = []
	for know_list in collected:
		y_data = []
		#itemがknow_listにあれば1を追加する
		for item in all_word_list:
			if item in know_list:
				y_data.append(int(1))
			else:
				y_data.append(int(0))
			
		for i in range(4):
			y_train.append(y_data)
				
	return y_train



#csvを読み込んでデータ作成	
def read_csv(csv_data):
	collected = []
	# ファイルを読み込みモードでオープン
	with open(csv_data, 'r', encoding = "shift-jis") as f:
		# 行ごとのリストを処理する
		for row in f:
			row = row.rstrip()
			row = row.replace('\"', '')
			row = row.replace(' ', '')
			row = row.replace('インスタントミニュチュア製造カメラ', 'インスタントミニチュア製造カメラ')
			row = row.replace('かならず実現するメモ帳', 'かならず実現する予定メモ帳')
			row = row.replace('穴掘り機', '穴ほり機')
			row = row.replace('重量ペンキ', '重力ペンキ')
			line = row.split(",")
			collected.append(line)
		del(collected[0])
			
			
	return collected




if __name__ == "__main__":

	collected = read_csv("himitsu_data_user.csv")
	print(collected)
	
	himitsu  = himitsu_data_gd.mk_allword_list()
	word_vec = himitsu_data_gd.mk_vec(himitsu)

	
	x_train  = mk_x_train(himitsu, word_vec, collected)
	y_train  = mk_y_train(himitsu, collected)
	
	print("[")
	for item in collected:
		print(item)
	print("]")
	
	print("[")
	for item in x_train:
		print(item)
	print("]\n")
	print("[")
	for i in y_train:
		print(i)
	print("]")
	print("len of x_train:", len(x_train))
	print("len of y_train:", len(y_train))
	print("len of correct lavel:",len(y_train[0]))
	
	
"""
	#模擬データでcollectedを生成
	collected = []
	for j in range(10):
		b = random.randint(8,50)
		user = random.sample(himitsu, b)
		
		collected.append(user)
"""		
	

	


