# /*    
 # * ServoTest.py 
 # * This is a test code  for BBG/BBB motor bridge cape Servo
 # *   
 # * Copyright (c) 2015 seeed technology inc.  
 # * Author      : Jiankai Li  
 # * Create Time:  Nov 2015
 # * Change Log : 
 # *
 # * The MIT License (MIT)
 # *
 # * Permission is hereby granted, free of charge, to any person obtaining a copy
 # * of this software and associated documentation files (the "Software"), to deal
 # * in the Software without restriction, including without limitation the rights
 # * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 # * copies of the Software, and to permit persons to whom the Software is
 # * furnished to do so, subject to the following conditions:
 # * 
 # * The above copyright notice and this permission notice shall be included in
 # * all copies or substantial portions of the Software.
 # * 
 # * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 # * THE SOFTWARE.
 # */

import MotorBridge
import time
ServoName   =  2
Frequency   =  50
Angle1      =  20
Angle2      =  160


    
if __name__=="__main__":
    motor = MotorBridge.MotorBridgeCape()
    motor.ServoInit(ServoName,Frequency)
    
    while True:
        print 'Servo Test'
        motor.ServoMoveAngle(ServoName,Angle1)
        time.sleep(2)
        motor.ServoMoveAngle(ServoName,Angle2)
        time.sleep(2)
