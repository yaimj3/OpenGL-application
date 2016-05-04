# Yoo, Minjung
# 1001-013-459
# 2016-05-02
# Assignment_05

import sys
import OpenGL

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy as np
import math as math
from copy import deepcopy

Angle = 0
#Incr = 1

# initialize global values
CAMERA_FILE = "cameras_05.txt"
INPUT_FILE = "pyramid_05.txt"
VERTICES = {}
FACE =[]
NEW_VERTICES ={}

#DRAW OBJECTS USING OPENGL FUNCTION
def draw():

    global NEW_VERTICES
    global FACE
    global INPUT_FILE

    fileName = INPUT_FILE
    size = len(NEW_VERTICES)
    #glNewList(1,GL_COMPILE)
    if fileName != "teapot_05.txt":
        #start drawing
        glNewList(1,GL_COMPILE)

        glBegin(GL_TRIANGLES)
        for i in range(1,size):

            x = float(NEW_VERTICES[i][0])
            y = float(NEW_VERTICES[i][1])
            z = float(NEW_VERTICES[i][2])
            glVertex3f(x,y,z)

        size = len(FACE)
        for i in range(0,size):

            #glColor3f(1,0,0)

            a = int(FACE[i][0])
            b = int(FACE[i][1])
            c = int(FACE[i][2])
            Vx = NEW_VERTICES[a]
            Vy = NEW_VERTICES[b]
            Vz = NEW_VERTICES[c]

            glVertex3f(float(Vx[0]), float(Vx[1]), float(Vx[2]))
            glVertex3f(float(Vy[0]), float(Vy[1]), float(Vy[2]))
            glVertex3f(float(Vz[0]), float(Vz[1]), float(Vz[2]))


    else:
        glNewList(1,GL_COMPILE)
        glBegin(GL_QUADS)
        for i in range(1,size):

            x = float(NEW_VERTICES[i][0])
            y = float(NEW_VERTICES[i][1])
            z = float(NEW_VERTICES[i][2])
            glVertex3f(x,y,z)

        size = len(FACE)
        for i in range(0,size):

            #glColor3f(1,0,0)

            a = int(FACE[i][0])
            b = int(FACE[i][1])
            c = int(FACE[i][2])
            d = int(FACE[i][3])


            Va = NEW_VERTICES[a]
            Vb = NEW_VERTICES[b]
            Vc = NEW_VERTICES[c]
            Vd = NEW_VERTICES[d]

            glVertex3f(float(Va[0]), float(Va[1]), float(Va[2]))
            glVertex3f(float(Vb[0]), float(Vb[1]), float(Vb[2]))
            glVertex3f(float(Vc[0]), float(Vc[1]), float(Vc[2]))
            glVertex3f(float(Vd[0]), float(Vd[1]), float(Vd[2]))


    glEnd()
    glEndList()

#CREATE 3D AXES
def create_3d_axes():

      glNewList(2,GL_COMPILE)
      glBegin(GL_LINES)
      glColor3f(1,0,0)
      glVertex3f(0,0,0)
      glVertex3f(2,0,0)
      glEnd()

      glBegin(GL_LINES)
      glColor3f(0,1,0)
      glVertex3f(0,0,0)
      glVertex3f(0,2,0)
      glEnd()

      glBegin(GL_LINES)
      glColor3f(0,0,1)
      glVertex3f(0,0,0)
      glVertex3f(0,0,2)
      glEnd()
      glEndList()
"""
# CREATE MULTIPLE WINDOW FRAMES TO DISPLAY
def display():
      global Angle

      w=glutGet(GLUT_WINDOW_WIDTH)
      h=glutGet(GLUT_WINDOW_HEIGHT)

      glScissor (0,0,w,h)
      glClearColor(0,0,0,0)
      glClear(GL_COLOR_BUFFER_BIT)

     #left-top :top camera
      glEnable(GL_SCISSOR_TEST)
      glScissor(int(0.1*w),int(0.6*h),int(0.3*w),int(0.3*h))
      glClearColor(0.4,0.4,0.6,0)
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()
      glFrustum(-1,1,-1,1,1,25)
      gluLookAt(0,4,0,0,-1,0,0,0,-1)
      glMatrixMode(GL_MODELVIEW)
      glViewport(int(0.1*w),int(0.6*h),int(0.3*w),int(0.3*h))
      glCallList(1)
      glPushMatrix()
      glLoadIdentity()
      glCallList(2)
      glPopMatrix()

      #left-bottom :front camera
      glEnable(GL_SCISSOR_TEST)
      glScissor(int(0.1*w),int(0.1*h),int(0.3*w),int(0.3*h))
      glClearColor(0.4,0.4,0.6,0)
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()
      glFrustum(-1,1,-1,1,1,25)
      gluLookAt(0,0,4,0,0,-1,0,1,0)
      glMatrixMode(GL_MODELVIEW)
      glViewport(int(0.1*w),int(0.1*h),int(0.3*w),int(0.3*h))
      glCallList(1)
      glPushMatrix()
      glLoadIdentity()
      glCallList(2)
      glPopMatrix()

      #right-top: perspective camera
      glScissor(int(0.5*w),int(0.5*h),int(0.25*w),int(0.25*h))
      glClearColor(0.4,0.4,0.6,0)
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()
      #glFrustum(-1,1,-1,1,1,30)
      #glOrtho(-1,1,-1,1,1,25)
      gluPerspective(45,0.67,5,20)
      gluLookAt(5,5,5,0,0,1,0,1,0)
      glMatrixMode(GL_MODELVIEW)
      glViewport(int(0.5*w),int(0.5*h),int(0.25*w),int(0.25*h))
      glCallList(1)
      glPushMatrix()
      glLoadIdentity()
      glCallList(2)
      glPopMatrix()

      #right-bottom : side camera
      glScissor(int(0.6*w),int(0.1*h),int(0.3*w),int(0.3*h))
      glClearColor(0.4,0.4,0.6,0)
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()
      #glOrtho(-2,2,-3,3,5,20)
      glFrustum(-1,1,-1,1,1,30)
      gluLookAt(4,0,0,0,0,0,0,1,0)
      glMatrixMode(GL_MODELVIEW)
      glViewport(int(0.6*w),int(0.1*h),int(0.3*w),int(0.3*h))
      glCallList(1)
      glPushMatrix()
      glLoadIdentity()
      glCallList(2)
      glPopMatrix()

      glFlush()
      glutSwapBuffers()

      glLoadIdentity()
"""

#LOAD CAMERA INFORMATION
def loadCamera(fileName):
    fileopen = open(fileName,'r')
    isParallel=[]
    window=[]
    viewport=[]
    eye=[]
    look=[]
    name=[]
    vup=[]

    for line in fileopen:
        index = line[0]
        tempStr = line[2:]

        if index is 't':
            if 'parallel' in tempStr:
                isParallel.append(True)
            else:
                isParallel.append(False)
        elif index is 'e':
            eye.append(tempStr.split())
        elif index is 'l':
            look.append(tempStr.split())
        elif index is 'u':
            vup.append(tempStr.split())
        elif index is 'w':
            window.append(tempStr.split())
        elif index is 'i':
            name.append(tempStr.strip('\r\n'))
        elif index is 's':
            viewport.append(tempStr.split())

    fileopen.close()

    global cameraInfo
    cameraInfo=[]

    size = len(isParallel)
    for i in range(0,size):
        cameraInfo.append([name[i],isParallel[i], eye[i], look[i], vup[i], window[i],viewport[i]]
        )

#LOAD OBJECT INFORMATION (VERTICES AND FACES)
def load_input_file(fileName):
    global FACE
    global VERTICES
    global NEW_VERTICES

    FACE =[]
    VERTICES ={}
    NEW_VERTICES={}
    #parse input data file
    fileopen = open(fileName,"r")
    temp = []
    i=0
    for line in fileopen:
        index = line[0]
        tempStr =line[2:]

        if index is 'v':
            i=i+1
            VERTICES[i]=tempStr.split()

        elif index is 'f':
            FACE.append(tempStr.split())
    fileopen.close()


    NEW_VERTICES = deepcopy(VERTICES)


#CREATE MULTIPLE WINDOW FRAMES AND OBJECTS USING OPENGL
def display():

    global cameraInfo
    global Angle

    w = glutGet(GLUT_WINDOW_WIDTH)
    h = glutGet(GLUT_WINDOW_HEIGHT)

    name=[]
    viewport=[]
    window =[]
    isParallel =[]
    eye=[]
    look=[]
    vup=[]

    size = len(cameraInfo)
    for i in range(0,size):
        name.append(cameraInfo[i][0])
        isParallel.append(cameraInfo[i][1])
        eye.append(cameraInfo[i][2])
        look.append(cameraInfo[i][3])
        vup.append(cameraInfo[i][4])
        viewport.append(cameraInfo[i][6])
        window.append(cameraInfo[i][5])


    glScissor (0,0,w,h)
    glClearColor(0,0,0,0)
    glClear(GL_COLOR_BUFFER_BIT)


    for i in range(0,size):

        camera_type = name[i]
        flag_parallel = isParallel[i]

        eye_x = float(eye[i][0])
        eye_y = float(eye[i][1])
        eye_z = float(eye[i][2])

        look_x = float(look[i][0])
        look_y = float(look[i][1])
        look_z = float(look[i][2])

        vup_x = float(vup[i][0])
        vup_y = float(vup[i][1])
        vup_z = float(vup[i][2])

        umin = float(window[i][0])
        umax = float(window[i][1])
        vmin = float(window[i][2])
        vmax = float(window[i][3])
        nmin = float(window[i][4])
        nmax = float(window[i][5])

        xmin = float(viewport[i][0])
        ymin = float(viewport[i][1])
        xmax = float(viewport[i][2])
        ymax = float(viewport[i][3])


        if camera_type == 'front':
            #left-bottom :front camera
            glEnable(GL_SCISSOR_TEST)
            glScissor(int(xmin*w),int(ymin*h),int((xmax-xmin)*w),int((ymax-ymin)*h))
            glClearColor(0.4,0.4,0.6,0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            if flag_parallel == False:
                glOrtho(umin,umax,vmin,vmax,nmin,nmax)
                #gluPerspective(45,float((umax-umin)/(vmax-vmin)),nmin,nmax)
            else:
                glFrustum(umin,umax,vmin,vmax,nmin,nmax)
            gluLookAt(eye_x,eye_y,eye_z,look_x,look_y,look_z,vup_x,vup_y,vup_z)
            glMatrixMode(GL_MODELVIEW)
            glViewport(int(xmin*w),int(ymin*h),int((xmax-xmin)*w),int((ymax-ymin)*h))
            glCallList(1)
            glPushMatrix()
            glLoadIdentity()
            glCallList(2)
            glPopMatrix()
        elif camera_type == 'top':
            glEnable(GL_SCISSOR_TEST)
            glScissor(int(xmin*w),int(ymin*h),int((xmax-xmin)*w),int((ymax-ymin)*h))
            glClearColor(0.4,0.4,0.6,0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            if flag_parallel == False:
                glOrtho(umin,umax,vmin,vmax,nmin,nmax)
                #gluPerspective(45,float((umax-umin)/(vmax-vmin)),nmin,nmax)
            else:
                glFrustum(umin,umax,vmin,vmax,nmin,nmax)
            gluLookAt(eye_x,eye_y,eye_z,look_x,look_y,look_z,vup_x,vup_y,vup_z)
            glMatrixMode(GL_MODELVIEW)
            glViewport(int(xmin*w),int(ymin*h),int((xmax-xmin)*w),int((ymax-ymin)*h))
            glCallList(1)
            glPushMatrix()
            glLoadIdentity()
            glCallList(2)
            glPopMatrix()

        elif camera_type == 'side':
            glScissor(int(xmin*w),int(ymin*h),int((xmax-xmin)*w),int((ymax-ymin)*h))
            glClearColor(0.4,0.4,0.6,0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            #glOrtho(-2,2,-3,3,5,20)
            if flag_parallel == False:
                glOrtho(umin,umax,vmin,vmax,nmin,nmax)
                #gluPerspective(45,float((umax-umin)/(vmax-vmin)),nmin,nmax)
            else:
                glFrustum(umin,umax,vmin,vmax,nmin,nmax)

            gluLookAt(eye_x,eye_y,eye_z,look_x,look_y,look_z,vup_x,vup_y,vup_z)
            glMatrixMode(GL_MODELVIEW)
            glViewport(int(xmin*w),int(ymin*h),int((xmax-xmin)*w),int((ymax-ymin)*h))
            glCallList(1)
            glPushMatrix()
            glLoadIdentity()
            glCallList(2)
            glPopMatrix()
        else:
            glScissor(int(xmin*w),int(ymin*h),int((xmax-xmin)*w),int((ymax-ymin)*h))
            glClearColor(0.4,0.4,0.6,0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            #glFrustum(-1,1,-1,1,1,30)
            #glOrtho(-1,1,-1,1,1,25)
            if flag_parallel == False:
                glOrtho(umin,umax,vmin,vmax,nmin,nmax)
                #gluPerspective(45,float((umax-umin)/(vmax-vmin)),nmin,nmax)
            else:
                glFrustum(umin,umax,vmin,vmax,nmin,nmax)
            gluLookAt(eye_x,eye_y,eye_z,look_x,look_y,look_z,vup_x,vup_y,vup_z)
            glMatrixMode(GL_MODELVIEW)
            glViewport(int(xmin*w),int(ymin*h),int((xmax-xmin)*w),int((ymax-ymin)*h))
            glCallList(1)
            glPushMatrix()
            glLoadIdentity()
            glCallList(2)
            glPopMatrix()



    glFlush()
    glutSwapBuffers()

    glLoadIdentity()

def rotate(angle,axis):
    global NEW_VERTICES
    cos = math.cos(math.radians(angle))
    sin = math.sin(math.radians(angle))

    if axis is 'x':
        rotate = np.matrix ( ((1,0,0,0), (0,cos,-sin,0),(0,sin,cos,0),(0,0,0,1)))
    elif axis is 'y':
        rotate = np.matrix ( ((cos,0,sin,0), (0,1,0,0),(-sin,0,cos,0),(0,0,0,1)))
    elif axis is 'z':
        rotate = np.matrix ( ((cos,-sin,0,0),(sin,cos,0,0),(0,0,1,0),(0,0,0,1)))

    for key in NEW_VERTICES:
        x = float(NEW_VERTICES[key][0])
        y = float(NEW_VERTICES[key][1])
        z = float(NEW_VERTICES[key][2])

        tempPoint = np.matrix(((x,y,z,1)))
        result = rotate * np.transpose(tempPoint)
        X = float(result[0][0])
        Y = float(result[1][0])
        Z = float(result[2][0])

        newPoint = [X,Y,Z]
        NEW_VERTICES[key] = newPoint

    draw()

def scale(rate):
    global NEW_VERTICES

    scale = np.matrix ( ( (rate,0,0,0), (0,rate,0,0), (0,0,rate,0), (0,0,0,1) ))

    for key in NEW_VERTICES:
        x = float(NEW_VERTICES[key][0])
        y = float(NEW_VERTICES[key][1])
        z = float(NEW_VERTICES[key][2])

        tempPoint = np.matrix(((x,y,z,1)))
        result = scale * np.transpose(tempPoint)
        X = float(result[0][0])
        Y = float(result[1][0])
        Z = float(result[2][0])

        newPoint = [X,Y,Z]
        NEW_VERTICES[key] = newPoint

    draw()

def update_projection():
    global cameraInfo
    size = len(cameraInfo)

    for i in range(0,size):
        temp = cameraInfo[i][1]
        if temp == False:
            temp = True
        else:
            temp = False
        cameraInfo[i][1] = temp

    display()

#FORWARD AND BACKWARD
def update_eye(rate, option):
    global cameraInfo
    size = len(cameraInfo)

    for i in range(0,size):

        #get distance between eye and look

        eye_x = float(cameraInfo[i][2][0])
        eye_y = float(cameraInfo[i][2][1])
        eye_z = float(cameraInfo[i][2][2])

        look_x = float(cameraInfo[i][3][0])
        look_y = float(cameraInfo[i][3][1])
        look_z = float(cameraInfo[i][3][2])

        dist_x = eye_x - look_x
        dist_y = eye_y - look_y
        dist_z = eye_z - look_z
        dist = math.sqrt( dist_x**2 + dist_y**2 + dist_z**2)

        if option =='f':
            eye_x = eye_x+(dist*rate)
            eye_y = eye_y+(dist*rate)
            eye_z = eye_z+(dist*rate)
        else:
            eye_x = eye_x-(dist*rate)
            eye_y = eye_y-(dist*rate)
            eye_z = eye_z-(dist*rate)

        cameraInfo[i][2] = [eye_x,eye_y,eye_z]

    display()

def update_eye2(key):
    global cameraInfo
    size = len(cameraInfo)

    for i in range(0,size):

        eye_x = float(cameraInfo[i][2][0])
        eye_y = float(cameraInfo[i][2][1])
        eye_z = float(cameraInfo[i][2][2])

        look_x = float(cameraInfo[i][3][0])
        look_y = float(cameraInfo[i][3][1])
        look_z = float(cameraInfo[i][3][2])

        dist_x = eye_x - look_x
        dist_y = eye_y - look_y
        dist_z = eye_z - look_z

        dist = math.sqrt( dist_x**2 + dist_y**2 + dist_z**2)



        #LEFT
        if key ==100:
            eye_x =eye_x + (dist*0.05)
            cameraInfo[i][2][0] = eye_x

        #UP
        elif key ==101:
            eye_y = eye_y + (dist*0.05)
            cameraInfo[i][2][1] = eye_y


        #RIGHT
        elif key == 102:
            eye_x = eye_x -(dist*0.05)
            cameraInfo[i][2][0] = eye_x

        #DOWN
        else:
            eye_y = eye_y - (dist*0.05)
            cameraInfo[i][2][1] = eye_y

        #cameraInfo[i][2] = [new_eye_x,new_eye_y,new_eye_z]

    display()

#SPECIAL KEY HANDLER
def spKeyHandler(Key, MouseX, MouseY):

    """
    100 - left
    102 - right
    101 - up
    103 - down
    """
    if Key is 100 or Key is 102:
        print("left/right")
        update_eye2(Key)

    elif Key is 101 or Key is 103:
        print("up/down")
        update_eye2(Key)
#REGULAR KEY HANDLER
def keyHandler(Key, MouseX, MouseY):

      global Angle
      global VERTICES
      global INPUT_FILE

      """
      if Key == b'f' or Key == b'F':
            print (b"Speeding Up")
            Incr = Incr + 1
      elif Key == b's' or Key == b'S':
            if Incr == 0:
                  print ("Stopped")
            else:
                  print ("Slowing Down")
                  Incr = Incr - 1

      """
      if Key is b'x' or Key is b'X':
          if Key is b'x':
              Angle = 5
          else:
              Angle = -5
          print("rotate around x-axis")
          rotate(Angle,'x')
      elif Key is b'y' or Key is b'Y':
          if Key is b'y':
              Angle = 5
          else:
              Angle = -5
          print("rotate around y-axis")
          rotate(Angle,'y')
      elif Key is b'z' or Key is b'Z':
          if Key is b'z':
              Angle = 5
          else:
              Angle = -5
          print("rotate around z-axis")
          rotate(Angle,'z')
      elif Key is b's' or Key is b'S':
          if Key is b's':
              rate = 1.05
          else:
              rate = 1/1.05
          #glScalef(scale,scale,scale)
          print("scale")
          scale(rate)
      elif Key is b'f' or Key is b'b':
          if Key is b'f':
              rate = 0.05
              print("forward")
          else:
              rate = 0.05/1.05
              print("backward")

          update_eye(rate, Key)
      elif Key is b'p':
          print("change parallel/perspective projection")
          update_projection()
      elif Key is b'n':
          filename = raw_input("Enter the file name to load: ")
          INPUT_FILE =filename

          load_input_file(INPUT_FILE)
          draw()
      elif Key == b'q' or Key == b'Q':
          print ("Exit the program")
          sys.exit()
      else:
          print ("Invalid Key",Key)



def timer(dummy):
      display()
      glutTimerFunc(30,timer,0)

def reshape(w, h):
      print ("Width=",w,"Height=",h)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
    glutInitWindowSize(640, 640)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Minjung Yoo Assignment_05")
    glClearColor(1,1,0,0)
    glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS);

    loadCamera(CAMERA_FILE)
    load_input_file(INPUT_FILE)
    glutDisplayFunc(display)
    glutSpecialFunc(spKeyHandler)
    glutKeyboardFunc(keyHandler)
    glutTimerFunc(300,timer,0)
    glutReshapeFunc(reshape)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    draw()
    create_3d_axes()
    glutMainLoop()

#START MAIN FUNCTION
main()
