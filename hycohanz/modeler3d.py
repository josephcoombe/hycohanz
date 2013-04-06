# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 22:34:02 2012

@author: radway
"""

from __future__ import division, print_function, unicode_literals, absolute_import

import warnings

from hycohanz.expression import Expression as Ex

warnings.simplefilter('default')

def assign_material(oEditor, partlist, MaterialName="vacuum", SolveInside=True):
    """
    Assign a material to the specified objects. Only the MaterialName and 
    SolveInside parameters of <AttributesArray> are supported.
    
    Parameters
    ----------
    oEditor : pywin32 COMObject
        The HFSS editor in which the operation will be performed.
    partlist : list
        List of part name strings to which the material is applied.
    
    Returns
    -------
    None
    """
    selectionsarray = ["NAME:Selections", 
                       "Selections:=", ','.join(partlist)]
    
    attributesarray = ["NAME:Attributes", 
                       "MaterialName:=", MaterialName, 
                       "SolveInside:=", SolveInside]
    
    oEditor.AssignMaterial(selectionsarray, attributesarray)

def create_circle(oEditor, xc, yc, zc, radius, 
                  WhichAxis='Z', 
                  NumSegments=0,
                  Name='Circle1',
                  Flags='',
                  Color=(132, 132, 193),
                  Transparency=0,
                  PartCoordinateSystem='Global',
                  MaterialName='"vacuum"',
                  Solveinside=True):
    """
    Create a circle primitive.
    
    Parameters
    ----------
    oEditor : pywin32 COMObject
        The HFSS editor in which the operation will be performed.
    xc : float or hycohanz Expression object
    yc : float or hycohanz Expression object
    zc : float or hycohanz Expression object
        The x, y, and z coordinates of the center of the circle.
    radius : float
        The radius of the circle.
    WhichAxis : str
        The axis normal to the circle.  Can be 'X', 'Y', or 'Z'.
    NumSegments : int
        If 0, the circle is not segmented.  Otherwise, the circle is 
        segmented into NumSegments sides.
    Name : str
        The requested name of the object.  If this is not available, HFSS 
        will assign a different name, which is returned by this function.
    Flags : str
        Flags associated with this object.  See HFSS help for details.
    Color : tuple of length=3
        RGB components of the circle
    Transparency : float between 0 and 1
        Fractional transparency.  0 is opaque and 1 is transparent.
    PartCoordinateSystem : str
        The name of the coordinate system in which the object is drawn.
    MaterialName : str
        Name of the material to assign to the object.  Name must be surrounded 
        by double quotes.
    SolveInside : bool
        Whether to mesh the interior of the object and solve for the fields 
        inside.
        
    Returns
    -------
    str
        The actual name of the created object.
    """
    circleparams = ["NAME:CircleParameters", 
                    "XCenter:=", Ex(xc).expr, 
                    "YCenter:=", Ex(yc).expr, 
                    "ZCenter:=", Ex(zc).expr, 
                    "Radius:=", Ex(radius).expr, 
                    "WhichAxis:=", str(WhichAxis), 
                    "NumSegments:=", str(NumSegments)]

    attributesarray = ["NAME:Attributes", 
                       "Name:=", Name, 
                       "Flags:=", Flags, 
                       "Color:=", "({r} {g} {b})".format(r=Color[0], g=Color[1], b=Color[2]), 
                       "Transparency:=", str(Transparency), 
                       "PartCoordinateSystem:=", PartCoordinateSystem, 
                       "MaterialName:=", MaterialName, 
                       "Solveinside:=", Solveinside]

    return oEditor.CreateCircle(circleparams, attributesarray)

def create_sphere(oEditor, x, y, z, radius,
                  Name="Sphere1",
                  Flags="",
                  Color=(132, 132, 193),
                  Transparency=0,
                  PartCoordinateSystem="Global",
                  UDMId="",
                  MaterialValue='"vacuum"',
                  SolveInside=True):
    """
    Create a sphere primitive.
    
    Parameters
    ----------
    oEditor : pywin32 COMObject
        The HFSS editor in which the operation will be performed.
    x : float or hycohanz Expression object
        x position in Cartesian coordinates.
    y : float or hycohanz Expression object
        y position in Cartesian coordinates.
    z : float or hycohanz Expression object
        z position in Cartesian coordinates.
    radius : float
        The sphere radius.
    Name : str
        The requested name of the object.  HFSS doesn't necessarily honor this.
    Flags : str
        Flags to attach to the object.  See the HFSS help for explanation 
        of this parameter.
    Color : tuple of ints
        The RGB indices corresponding to the desired color of the object.
    Transparency : float between 0 and 1
        Fractional transparency.  0 is opaque and 1 is transparent.
    PartCoordinateSystem : str
        The name of the coordinate system in which the object is drawn.
    UDMId : str
        Unknown use.  See HFSS documentation for explanation.
    MaterialValue : str
        Name of the material to assign to the object
    SolveInside : bool
        Whether to mesh the interior of the object and solve for the fields 
        inside.
        
    Returns
    -------
    part : str
        The actual name assigned by HFSS to the part.
        
    """
    sphereparametersarray = ["NAME:SphereParameters", 
                             "XCenter:=", Ex(x).expr, 
                             "YCenter:=", Ex(y).expr, 
                             "ZCenter:=", Ex(z).expr, 
                             "Radius:=", Ex(radius).expr]
    
    attributesarray = ["NAME:Attributes", 
                       "Name:=",  Name, 
                       "Flags:=", Flags, 
                       "Color:=", "({r} {g} {b})".format(r=Color[0], g=Color[1], b=Color[2]), 
                       "Transparency:=", Transparency, 
                       "PartCoordinateSystem:=", PartCoordinateSystem, 
                       "UDMId:=", UDMId, 
                       "MaterialValue:=", MaterialValue, 
                       "SolveInside:=", SolveInside]
    
    part = oEditor.CreateSphere(sphereparametersarray, attributesarray)
    
    return part
