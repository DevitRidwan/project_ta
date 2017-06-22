from django.shortcuts import render
from django.contrib.auth.models import User

def AddUser(profile):
	if profile.status_user == False:
		nama = str(profile.nama)
		name = nama[0]
		hari = str(profile.tgl_lahir.day)
		if len(hari) < 2:
			hari="0"+hari
		bulan = str(profile.tgl_lahir.month)
		if len(bulan) < 2:
			bulan="0"+bulan
		tahun = str(profile.tgl_lahir.year)[2] + str(profile.tgl_lahir.year)[3]
		get_nama = [pos for pos, nchar in enumerate(nama) if nchar == ' ']
		get_tgl = hari+bulan+tahun
		for user in get_nama:
			name += nama[user+1]

		username = name + str(profile.pk) + get_tgl
		password = User.objects.make_random_password()

		#create User
		profile.username = username
		profile.save()
		user_create = User(username=username)
		user_create.save()
		user_create.set_password(password)
		user_create.save()

		return render(request, 'add-user.html', {'username':username, 'password':password})
	else:
		message = str(profile.nama) + ' sudah terdaftar'
		return render(request, 'add-user.html', {'message':message})