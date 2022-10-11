#Pedro Buganeme Müller - 12560105
print('Programa para simular a projeção em 3D')
print("Insira os valores para a câmera 1")
xcam1 = float(input('X = '))
ycam1 = float(input('Y = '))
zcam1 = float(input('Z = '))
print('\n')

print("Insira os valores para a câmera 2")
xcam2 = float(input('X = '))
ycam2 = float(input('Y = '))
zcam2 = float(input('Z = '))
print('\n')

print("Insira onde a é projetada a câmera 1")
xproj1 = float(input('X = '))
yproj1 = float(input('Y = '))
zproj1 = float(input('Z = '))
print('\n')

print("Insira onde a é projetada a câmera 2")
xproj2 = float(input('X = '))
yproj2 = float(input('Y = '))
zproj2 = float(input('Z = '))
print('\n')


vetorcam1 = [(xcam1), (ycam1), (zcam1)]
vetorcam2 = [(xcam2), (ycam2), (zcam2)]
vetorproj1 = [(xproj1), (yproj1), (zproj1)]
vetorproj2 = [(xproj2), (yproj2), (zproj2)]

mr1xy = (vetorproj1[1] - vetorcam1[1]) / (vetorproj1[0] - vetorcam1[0])
mr1xz = (vetorproj1[2] - vetorcam1[2]) / (vetorproj1[0] - vetorcam1[0])
mr1zy = (vetorproj1[1] - vetorcam1[1]) / (vetorproj1[2] - vetorcam1[2])

mr2xy = (vetorproj2[1] - vetorcam2[1]) / (vetorproj2[0] - vetorcam2[0])
mr2xz = (vetorproj2[2] - vetorcam2[2]) / (vetorproj2[0] - vetorcam2[0])
mr2zy = (vetorproj2[1] - vetorcam2[1]) / (vetorproj2[2] - vetorcam2[2]) 

x1 = (ycam2 + (mr1xy * xcam1) - (mr2xy * xcam2) - ycam1) / (mr1xy - mr2xy)
x2 = (zcam2 + (mr1xz * xcam1) - (mr2xz * xcam2) - zcam1) / (mr1xz - mr2xz)
y1 = ((mr1xy * x1) - (mr1xy * xcam1) + ycam1)
z2 = (ycam2 + (mr1zy * zcam1) - (mr2zy * zcam2) - ycam1) / (mr1zy - mr2zy)
y2 = ((mr1zy * z2) - (mr1zy * zcam1) + ycam1)
z1 = ((mr1xz * x2) - (mr1xz * xcam1) + zcam1)

x = (x1 + x2)/2
y= (y1 + y2)/2
z= (z1 + z2)/2


#Comandos para gerar o gráfico e editá-lo
from turtle import onclick
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.set_title ('Gráfico 3D de projeção', fontsize = 20)
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')

X = [xcam1, x, xproj1]
Y = [ycam1, y, yproj1]
Z = [zcam1, z, zproj1]

X2 = [xcam2, x, xproj2]
Y2 = [ycam2, y, yproj2]
Z2 = [zcam2, z, zproj2]

plt.plot(X, Y, Z, color = 'red')
plt.plot(X2, Y2, Z2, color = 'Green')

plt.show()