"""chainplan Rotation Computation,"""
#2022-7-28 15:19:33
import numpy as np

EXTREME_SMALL_NUMBER_4_ROTATION_COMPUTATION = 0.000000001

def FromPointer2Axis_Angle(Pointer,origin_pointer = np.array([0,1,0])):
    # Pointer must be an 3-dimensional ndarray
    # Return value : rotation_value, rotation_axis
    
    Pointer_2_norm = np.linalg.norm(Pointer)
    # if Pointer_2_norm <  EXTREME_SMALL_NUMBER_4_ROTATION_COMPUTATION and Pointer_2_norm > - EXTREME_SMALL_NUMBER_4_ROTATION_COMPUTATION
    normailized_pointer = Pointer / (Pointer_2_norm + EXTREME_SMALL_NUMBER_4_ROTATION_COMPUTATION)

    # print ('$$$ normailized_pointer:',normailized_pointer)
    rotation_axis  = np.cross(origin_pointer, normailized_pointer)
    rotation_value = np.pi

    # print('rotation_axis:',rotation_axis)

    rotation_axis_norm         = np.linalg.norm(rotation_axis)
    normailized_rotation_axis  = rotation_axis / (rotation_axis_norm \
                                                  + EXTREME_SMALL_NUMBER_4_ROTATION_COMPUTATION)
    # print('$$$ rotation_axis_norm:', rotation_axis_norm)

    if rotation_axis_norm < EXTREME_SMALL_NUMBER_4_ROTATION_COMPUTATION:
        normailized_rotation_axis = np.array([1,0,0])
        # rotation_value = np.pi
        return np.append(rotation_value, normailized_rotation_axis)


    cosine_value   = np.dot(normailized_pointer,origin_pointer)
    # print('normailized_rotation_axis:',normailized_rotation_axis)
    # print('cosine_value:',cosine_value )
    rotation_value = np.arccos(cosine_value)

    return np.append(normailized_rotation_axis, rotation_value)
###From a 3D pointer we calculate the axis-angle value