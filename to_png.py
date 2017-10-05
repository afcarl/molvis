#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Gaussian Cube Reader'
dtcube = GaussianCubeReader(FileName='/Users/ian/vmd/pfe/Dt.cube')

# create a new 'Gaussian Cube Reader'
eSPcube = GaussianCubeReader(FileName='/Users/ian/vmd/pfe/ESP.cube')

# set active source
SetActiveSource(dtcube)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [396, 552]

# show data in view
dtcubeDisplay = Show(dtcube, renderView1)
# trace defaults for the display properties.
dtcubeDisplay.Representation = 'Molecule'

# reset view to fit data
renderView1.ResetCamera()

# show color bar/color legend
dtcubeDisplay.SetScalarBarVisibility(renderView1, True)

# show data in view
dtcubeDisplay_1 = Show(OutputPort(dtcube, 1), renderView1)
# trace defaults for the display properties.
dtcubeDisplay_1.Representation = 'Outline'
dtcubeDisplay_1.ColorArrayName = ['POINTS', '']
dtcubeDisplay_1.OSPRayScaleArray = 'Property: Dt'
dtcubeDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
dtcubeDisplay_1.SelectOrientationVectors = 'None'
dtcubeDisplay_1.ScaleFactor = 6.9
dtcubeDisplay_1.SelectScaleArray = 'Property: Dt'
dtcubeDisplay_1.GlyphType = 'Arrow'
dtcubeDisplay_1.GlyphTableIndexArray = 'Property: Dt'
dtcubeDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
dtcubeDisplay_1.PolarAxes = 'PolarAxesRepresentation'
dtcubeDisplay_1.ScalarOpacityUnitDistance = 1.735365729852697
dtcubeDisplay_1.Slice = 31

# show data in view
eSPcubeDisplay = Show(eSPcube, renderView1)
# trace defaults for the display properties.
eSPcubeDisplay.Representation = 'Molecule'

# show color bar/color legend
eSPcubeDisplay.SetScalarBarVisibility(renderView1, True)

# show data in view
eSPcubeDisplay_1 = Show(OutputPort(eSPcube, 1), renderView1)
# trace defaults for the display properties.
eSPcubeDisplay_1.Representation = 'Outline'
eSPcubeDisplay_1.ColorArrayName = ['POINTS', '']
eSPcubeDisplay_1.OSPRayScaleArray = 'Property: ESP'
eSPcubeDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
eSPcubeDisplay_1.SelectOrientationVectors = 'None'
eSPcubeDisplay_1.ScaleFactor = 6.9
eSPcubeDisplay_1.SelectScaleArray = 'Property: ESP'
eSPcubeDisplay_1.GlyphType = 'Arrow'
eSPcubeDisplay_1.GlyphTableIndexArray = 'Property: ESP'
eSPcubeDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
eSPcubeDisplay_1.PolarAxes = 'PolarAxesRepresentation'
eSPcubeDisplay_1.ScalarOpacityUnitDistance = 1.735365729852697
eSPcubeDisplay_1.Slice = 31

# update the view to ensure updated data information
renderView1.Update()

# find source
dtcube_1 = FindSource('Dt.cube')

# create a new 'Contour'
contour1 = Contour(Input=OutputPort(dtcube_1,1))
contour1.ContourBy = ['POINTS', 'Property: Dt']
contour1.Isosurfaces = [69.45500183549095]
contour1.PointMergeMethod = 'Uniform Binning'

# Properties modified on contour1
contour1.Isosurfaces = [0.002]

# show data in view
contour1Display = Show(contour1, renderView1)
# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = [None, '']
contour1Display.OSPRayScaleArray = 'Normals'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = 5.507733917236329
contour1Display.SelectScaleArray = 'None'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'None'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'
contour1Display.GaussianRadius = 2.7538669586181643
contour1Display.SetScaleArray = [None, '']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = [None, '']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'

# update the view to ensure updated data information
renderView1.Update()

# find source
eSPcube_1 = FindSource('ESP.cube')

# create a new 'Resample With Dataset'
resampleWithDataset1 = ResampleWithDataset(Input=OutputPort(eSPcube_1,1),
    Source=contour1)

# get color transfer function/color map for 'PropertyESP'
propertyESPLUT = GetColorTransferFunction('PropertyESP')

# show data in view
resampleWithDataset1Display = Show(resampleWithDataset1, renderView1)
# trace defaults for the display properties.
resampleWithDataset1Display.Representation = 'Surface'
resampleWithDataset1Display.ColorArrayName = ['POINTS', 'Property: ESP']
resampleWithDataset1Display.LookupTable = propertyESPLUT
resampleWithDataset1Display.OSPRayScaleArray = 'Property: ESP'
resampleWithDataset1Display.OSPRayScaleFunction = 'PiecewiseFunction'
resampleWithDataset1Display.SelectOrientationVectors = 'None'
resampleWithDataset1Display.ScaleFactor = 5.507733917236329
resampleWithDataset1Display.SelectScaleArray = 'Property: ESP'
resampleWithDataset1Display.GlyphType = 'Arrow'
resampleWithDataset1Display.GlyphTableIndexArray = 'Property: ESP'
resampleWithDataset1Display.DataAxesGrid = 'GridAxesRepresentation'
resampleWithDataset1Display.PolarAxes = 'PolarAxesRepresentation'
resampleWithDataset1Display.GaussianRadius = 2.7538669586181643
resampleWithDataset1Display.SetScaleArray = ['POINTS', 'Property: ESP']
resampleWithDataset1Display.ScaleTransferFunction = 'PiecewiseFunction'
resampleWithDataset1Display.OpacityArray = ['POINTS', 'Property: ESP']
resampleWithDataset1Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(OutputPort(eSPcube, 1), renderView1)

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
resampleWithDataset1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
propertyESPLUT.RescaleTransferFunction(-0.0565273, 0.159)

# get opacity transfer function/opacity map for 'PropertyESP'
propertyESPPWF = GetOpacityTransferFunction('PropertyESP')

# Rescale transfer function
propertyESPPWF.RescaleTransferFunction(-0.0565273, 0.159)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [107.59699888881308, 23.59012667657415, -57.507272680761304]
renderView1.CameraFocalPoint = [32.999999046325684, 34.49999713897705, 31.000000953674316]
renderView1.CameraViewUp = [0.19001350376679654, -0.9421065764899228, 0.2762789657587113]
renderView1.CameraParallelScale = 30.59271872663042

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).