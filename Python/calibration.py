#!/usr/bin/env python
# encoding: utf-8
"""
calibration.py

Created by Jonathan Whitmore on 2010-05-03.
Modified: 2010-05-31
"""
version = 1.0

from config_calibration import *

# =============
# = Constants =
# =============
c_light = 299792458.

def initial_shift(fmultiple,fshift,fsigma):
  better_flx = starting_flx * fmultiple
  better_kernel = normal_gaussian(gauss_elements,fsigma)
  better_tck = si.splrep(slice_iow, np.convolve(better_kernel,\
                         slice_iof, mode='same'))
  better_y2 = si.splev(wav+fshift,better_tck)
  return sum((better_y2 - better_flx) ** 2 / \
             (fmultiple * err / con) ** 2 )

def fullordershift(fmultiple,fshift,fsigma):
  better_flx = starting_flx * fmultiple
  better_kernel = normal_gaussian(gauss_elements,fsigma)
  better_tck = si.splrep(slice_iow, np.convolve(better_kernel,\
                         slice_iof, mode='same'))
  better_y2 = si.splev(wav+fshift,better_tck)
  return (better_y2 - better_flx) ** 2 / \
             (fmultiple * err / con) ** 2 

def continuum_shift(fmultiple,fshift,fsigma,cmultiple):
  better_flx = flx / (con + con * cmultiple) * fmultiple
  better_kernel = normal_gaussian(gauss_elements,fsigma)
  better_tck = si.splrep(slice_iow, np.convolve(better_kernel,\
                         slice_iof, mode='same'))
  better_y2 = si.splev(wav+fshift,better_tck)
  return sum((better_y2 - better_flx) ** 2 / \
             (fmultiple * err / (con + con * cmultiple)) ** 2 )

#
def continuumshiftarray(fmultiple,fshift,fsigma,cmultiple):
  better_flx = flx / (con + con * cmultiple) * fmultiple
  better_kernel = normal_gaussian(gauss_elements,fsigma)
  better_tck = si.splrep(slice_iow, np.convolve(better_kernel,\
                         slice_iof, mode='same'))
  better_y2 = si.splev(wav+fshift,better_tck)
  return (better_y2 - better_flx) ** 2 / \
             (fmultiple * err / (con + con * cmultiple)) ** 2 


def second_shift(fmultiple,fshift,fsigma,fskew):
  better_flx = starting_flx * fmultiple
  better_kernel = normal_skew_gaussian(gauss_elements,fsigma,fskew)
  better_tck = si.splrep(slice_iow, np.convolve(better_kernel,\
                         slice_iof, mode='same'))
  better_y2 = si.splev(wav+fshift,better_tck)
  return sum((better_y2 - better_flx) ** 2 / \
             (fmultiple * err / con) ** 2 )

#
def skewshiftarray(fmultiple,fshift,fsigma,fskew):
  better_flx = starting_flx * fmultiple
  better_kernel = normal_skew_gaussian(gauss_elements,fsigma,fskew)
  better_tck = si.splrep(slice_iow, np.convolve(better_kernel,\
                         slice_iof, mode='same'))
  better_y2 = si.splev(wav+fshift,better_tck)
  return (better_y2 - better_flx) ** 2 / \
             (fmultiple * err / con) ** 2 


# bin-shifting fmultiple,fshift,fsigma
def shiftperbin(i,fmultiple,fshift,fsigma):
  better_flx = starting_flx[whit_index[int(i)]] * fmultiple
  better_kernel = normal_gaussian(gauss_elements,fsigma)
  better_tck = si.splrep(slice_iow, np.convolve(better_kernel,\
                         slice_iof, mode='same'))
  better_y2 = si.splev(wav[whit_index[int(i)]]+fshift, better_tck)
  return sum((better_y2 - better_flx) ** 2 / \
              (fmultiple * starting_err[whit_index[int(i)]] ) ** 2)
                # (fmultiple * err[whit_index[int(i)]] / con[whit_index[int(i)]]) ** 2)

#
def shiftperbinarray(i,fmultiple,fshift,fsigma):
  better_flx = starting_flx[whit_index[int(i)]] * fmultiple
  better_kernel = normal_gaussian(gauss_elements,fsigma)
  better_tck = si.splrep(slice_iow, np.convolve(better_kernel,\
                         slice_iof, mode='same'))
  better_y2 = si.splev(wav[whit_index[int(i)]]+fshift, better_tck)
  return (better_y2 - better_flx) ** 2 / \
              (fmultiple * err[whit_index[int(i)]] / con[whit_index[int(i)]]) ** 2

#   
def plotresidualshiftperbin(fshift,i,fmultiple,fsigma):
  better_flx = starting_flx[whit_index[int(i)]] * fmultiple
  better_kernel = normal_gaussian(gauss_elements,fsigma)
  better_tck = si.splrep(slice_iow, np.convolve(better_kernel,\
                         slice_iof, mode='same'))
  better_y2 = si.splev(wav[whit_index[int(i)]]+fshift, better_tck)
  pl.plot((better_y2 - better_flx) )
  return

#   
def plotsidebyside(i):
  pl.plot(wav[fitbinindex],better_y2,wav[fitbinindex],flx[fitbinindex] * fitbinmultiple)
    
def plotcontinuum_shift(fmultiple,fshift,fsigma,cmultiple):
  better_flx = flx / (con + con * cmultiple) * fmultiple
  better_kernel = normal_gaussian(gauss_elements,fsigma)
  better_tck = si.splrep(slice_iow, np.convolve(better_kernel,\
                         slice_iof, mode='same'))
  better_y2 = si.splev(wav+fshift,better_tck)
  return sum((better_y2 - better_flx) ** 2 / \
             (fmultiple * err / (con + con * cmultiple)) ** 2 )

def skewshiftperbin(fshift,i,fmultiple,fsigma,fskew):
  better_flx = starting_flx[whit_index[int(i)]] * fmultiple
  better_kernel = normal_skew_gaussian(gauss_elements,fsigma,fskew)
  better_tck = si.splrep(slice_iow, np.convolve(better_kernel,\
                         slice_iof, mode='same'))
  better_y2 = si.splev(wav[whit_index[int(i)]]+fshift, better_tck)
  return sum((better_y2 - better_flx) ** 2 / \
              (fmultiple * starting_err[whit_index[int(i)]]) ** 2)

#

CalibrationSummaryDir = "Summary/calibration."

# ====================
# = Read in FTS Data =
# ====================

# FTSReader = csv.reader(open(FTSFile), delimiter=' ')
# iow = []
# iof = []
# for row in FTSReader:
#     iow.append(float(row[0]))
#     iof.append(float(row[1]))
# 
# iow = np.array(iow)
# iof = np.array(iof)
iow, iof = np.loadtxt(FTSFile, unpack=True)

today = datetime.date.today()
CalibrationLogFile = "Logs/calibration." + str(today) + ".ascii"
CalibrationLogFileHandle = open(CalibrationLogFile, 'a')    

print "Beginning calibration analysis of data..."

for core_exposure in exposures_to_analyze:
  CalibrationDataList = glob.glob(OutputContinuumDir + astro_object + "." + core_exposure + "*")
  CalibrationDataList.sort()
  print datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

  CalibrationSummaryFileHandle = open(CalibrationSummaryDir + astro_object + "." + core_exposure + ".ascii",'w')
  print >>CalibrationSummaryFileHandle, str("#astro_object, weighted_av(velocity_fit,velocity_err), weighted_std(velocity_fit,velocity_err), fitordermultiple, fitordermultiple_err, fitordershift, fitordershift_err, fitordersigma, fitordersigma_err, order_velocity, FWHM, (FWHM_err1-FWHM_err2)/2.0")
  for CalibrationDataFile in CalibrationDataList:
    # #   Iterate over the Data files
    # wav = []
    # flx = []
    # err = []
    # con = []
    # pix = []
    # 
    # CalibrationDataReader = csv.reader(open(CalibrationDataFile), delimiter=' ')
    # for row in CalibrationDataReader:
    #   wav.append(float(row[0]))
    #   flx.append(float(row[1]))
    #   err.append(float(row[2]))
    #   con.append(float(row[3]))
    #   if len(row) > 4:
    #     pix.append(float(row[4]))
    # 
    # wav = np.array(wav)
    # flx = np.array(flx)
    # err = np.array(err)
    # con = np.array(con)
    # pix = np.array(pix)
    try: 
      wav, flx, err, con = np.loadtxt(CalibrationDataFile, unpack=True)
    except:
      try:
        wav, flx, err, con, pix = np.loadtxt(CalibrationDataFile, unpack=True)
      except:
        continue
    if len(wav) < 100:
      print "Not a big enough file, skipping..."
      continue

    # ================================================
    # = Logic Test to see if file overlaps FTS data =
    # ================================================
    if(wav[0] < iow[0]+80 or wav[-1] > iow[-1] - 100):
      print CalibrationDataFile, "is outside of overlap"
      continue
    
    # =================================
    # = Slice FTS to manageable size  =
    # =================================
    slice_iow = iow[np.where(iow > wav[0] - 10)]
    slice_iow = slice_iow[np.where(slice_iow < wav[-1] + 10)]
    slice_iof = iof[np.where(iow > wav[0] - 10)]
    slice_iof = slice_iof[np.where(slice_iow < wav[-1] + 10)]

    # Divide continuum out from input file
    starting_flx = flx / con
    starting_err = err / con
    
    firstsplit = CalibrationDataFile.split("/")
    secondsplit = firstsplit[-1].split(".")
    naming = "." + secondsplit[1] + "." + secondsplit[2] + "." + secondsplit[3] 
    nodotnaming = secondsplit[1] + "." + secondsplit[2] + "." + secondsplit[3] 
    # ======================================
    # = Initial Shift; Kernel Size finding =
    # ======================================

    m = mi.Minuit(initial_shift,fmultiple=0.82,fshift=0.01,\
                         fsigma=sigma,strategy=2)
                         # fsigma=15.,strategy=2)
    
    # TODO make this fsigma come from configuration file
    # TODO exception -- check if sigma negative -- if so, rerun fit with all fit parameters and negative sigma.
    # m.printMode=1
    m.migrad()
    #m.minos()
    order_velocity = c_light / wav[len(wav)/2]
    
    fitordermultiple = m.values["fmultiple"]
    fitordermultiple_err = m.errors["fmultiple"]
    
    fitordershift = m.values["fshift"]
    fitordershift_err = m.errors["fshift"]
    
    fitordersigma = m.values["fsigma"]
    fitordersigma_err = m.errors["fsigma"]
    
    print "\n",CalibrationDataFile, "\nShift: ", round(fitordershift * order_velocity,2), "m/s", \
            round(fitordershift_err * order_velocity,4), "m/s"
    print "Sigma: ", round(fitordersigma,2), round(fitordersigma_err,4)
    
    orderchisquarearray = fullordershift(fitordermultiple,fitordershift,fitordersigma)
    orderchisquare = np.sum(orderchisquarearray)
    DOF = 3
    print "Chi-Square: ", round(orderchisquare,2), "Chi-Sq/DOF: ", round(orderchisquare / (len(orderchisquarearray) - DOF),4)
    titlestr = nodotnaming + " Total Chi-Square: " + str(round(orderchisquare,2)) + \
        " Chi-Sq/DOF: " + str(round(orderchisquare / (len(orderchisquarearray) - DOF),2))
    pl.title(titlestr)        
    pl.plot(wav,fullordershift(fitordermultiple,fitordershift,fitordersigma))
    pl.xlabel("Wavelength in Angstroms")
    pl.ylabel("Chi-Square")
    pl.savefig(PdfQAOrderChiSquareDir + astro_object + naming + ".pdf")
    pl.savefig(PsQAOrderChiSquareDir + astro_object + naming + ".eps")
    pl.close()
    # Warning if constraining fitting function
    if gauss_elements/fitordersigma < 7.5:
      print "Warning: You should use a larger gaussian window\nYour current array is: ", gauss_elements
      print "Your current sigma is: ", fitordersigma, \
          " and elements/sigma: ", gauss_elements/fitordersigma
    

    # ========================================
    # = Create the bins and structure needed =
    # ========================================

    whit_index = []
    whit_step = wav[0] * step * 1000.0 / c_light
    for i in np.arange(wav[0],wav[-1], whit_step ):
      temp = i + i * bin_size * 1000.0 / c_light
      if len(np.where(wav[np.where(wav < temp)] > i )[0]) > 100 :
        whit_index.append(np.where(wav[np.where(wav < temp)[0]] > i ))
    
    wav_bin_av = []
    calib_fit = []
    calib_err = []
    resolution_fit = []
    resolution_err = []
    bin_call = []
    pix_average = []

    for i in np.arange(len(whit_index)):
      if(len(wav[whit_index[i]]) < 100):
        continue
      bin_call = mi.Minuit(shiftperbin,\
        i=i,\
        fix_i=True,\
        fmultiple=fitordermultiple,\
        fix_fmultiple=True,\
        fshift=fitordershift,\
        fsigma=fitordersigma,\
        # fix_fsigma=True,\ #test commented 
        strategy=2)
      try:
        bin_call.migrad()
      except:
        print "Bin Broke! Moving on. Wavelength region: ", wav[whit_index[i]][0], wav[whit_index[i]][-1]
        continue
        
      fitbinmultiple = bin_call.values["fmultiple"]
      fitbinshift =    bin_call.values["fshift"]
      fitbinsigma =    bin_call.values["fsigma"]
      fitbinindex =    whit_index[i]
      
      lamb = np.average(wav[fitbinindex])
      midpoint = np.argmin( np.abs( [ slice_iow - lamb ] ) )
      if len(wav) == len(pix):
        temp_pix = np.average(pix[fitbinindex])
      FWHM_prefactor = 2.0 * np.sqrt( 2.0 * np.log( 2.0 ) )
      
      # Full difference across considered lambdas
      full_lambda = slice_iow[midpoint + gauss_elements /2 ] - slice_iow[midpoint - gauss_elements/2]
      
      sigma_lambda = full_lambda * (fitbinsigma / gauss_elements)
      sigma_err_plus = full_lambda * (fitbinsigma + bin_call.errors["fsigma"]) / gauss_elements
      sigma_err_minus = full_lambda * (fitbinsigma - bin_call.errors["fsigma"]) / gauss_elements
      FWHM = FWHM_prefactor * sigma_lambda 
      FWHM_err1 = FWHM_prefactor * sigma_err_plus
      FWHM_err2 = FWHM_prefactor * sigma_err_minus

      wav_bin_av.append(lamb)
      calib_fit.append(fitbinshift)    
      calib_err.append(bin_call.errors["fshift"])
      resolution_fit.append( lamb / FWHM )
      resolution_err.append( np.abs( lamb/FWHM_err1 - lamb/FWHM_err2) /2.0 ) 
      if len(wav) == len(pix):
        pix_average.append(temp_pix)
      if i == len(whit_index)/2:
        binchisquarearray = shiftperbinarray(i,fitbinmultiple,fitbinshift,fitbinsigma)
        binchisquare = np.sum(binchisquarearray)
        plot_better_g = ss.gaussian(gauss_elements,fitbinsigma)
        better_kernel = plot_better_g / sum(plot_better_g)
        better_tck = si.splrep(slice_iow, np.convolve(better_kernel,\
                               slice_iof, mode='same'))
        better_y2 = si.splev(wav[whit_index[int(i)]]+fitbinshift,better_tck)
        
        pl.plot(wav[fitbinindex],flx[fitbinindex] * fitbinmultiple / con[fitbinindex],label=spectrograph)
        tempx = pl.xlim()
        pl.plot(wav[fitbinindex],better_y2,label="FTS")
        pl.xlim(tempx)
        pl.legend()
        pl.ylabel("Normalized Flux")
        pl.xlabel("Wavelength in Angstroms")
        titlestr = nodotnaming + " Mid-order Bin Fit-check"
        pl.title(titlestr)
        PdfQABinOverlayFile = PdfQABinOverlayDir + astro_object + naming + ".pdf"
        PsQABinOverlayFile = PsQABinOverlayDir + astro_object + naming + ".eps"
        pl.savefig(PdfQABinOverlayFile)
        pl.savefig(PsQABinOverlayFile)
        pl.close()
        
    
    wav_bin_av = np.array(wav_bin_av) 
    calib_fit = np.array(calib_fit)
    calib_err = np.array(calib_err)
    resolution_fit = np.array(resolution_fit)
    resolution_err = np.array(resolution_err)
    pix_average = np.array(pix_average)
    
    
    OutputCalibrationFile = OutputCalibrationDir + astro_object + naming + ".ascii"
    OutputResolutionFile = OutputResolutionDir + astro_object + naming + ".ascii" 

    print >>CalibrationLogFileHandle, CalibrationDataFile, wav[len(wav)/2], fitordershift * order_velocity, \
            fitordershift_err * order_velocity
    
    velocity_fit = c_light * calib_fit / wav_bin_av
    velocity_err = c_light * calib_err / wav_bin_av
    

    print >>CalibrationSummaryFileHandle, astro_object + naming, weighted_av(velocity_fit,velocity_err), \
        weighted_std(velocity_fit,velocity_err), \
        fitordermultiple,  fitordermultiple_err, \
        fitordershift, fitordershift_err, fitordersigma, fitordersigma_err, order_velocity, \
        FWHM, (FWHM_err1 - FWHM_err2) / 2.0
    
    # # moved to calibration-plot.py
    if(len(calib_fit) > 0):
      PdfCalibrationFile = PdfCalibrationDir + astro_object + naming + ".pdf" 
      PsCalibrationFile = PsCalibrationDir + astro_object + naming + ".eps" 
  
      titlestr = "Exposure: " + secondsplit[1] + " Chip: " + secondsplit[2] + " Order: " + secondsplit[3]
  
      pl.subplot(311)
      pl.ylabel("Flux")
      pl.title(titlestr)
      pl.plot(wav,flx * fitordermultiple,wav,err * fitordermultiple)
      temp = pl.xlim()
      pl.subplot(312)
      pl.ylabel("v_cal (m/s)")
      pl.errorbar(wav_bin_av,velocity_fit,yerr=velocity_err)
      pl.plot(wav_bin_av,np.zeros(len(wav_bin_av)))
      pl.xlim(temp)
      pl.subplot(313)
      pl.ylabel("R value")
      pl.errorbar(wav_bin_av,resolution_fit,yerr=resolution_err)
      pl.xlim(temp)
      pl.savefig(PdfCalibrationFile)
      pl.savefig(PsCalibrationFile)
      pl.close()

    OutputCalibrationFileHandle = open(OutputCalibrationFile, 'w')
    print "Weighted Average: ", round(weighted_av(velocity_fit,velocity_err),2), "m/s"
    print "Weighted std: ", round(weighted_std(velocity_fit,velocity_err),2), "m/s"
    
    for j in range(len(wav_bin_av)):
      if len(wav) == len(pix):
        print >>OutputCalibrationFileHandle, wav_bin_av[j], velocity_fit[j], velocity_err[j], \
                resolution_fit[j], resolution_err[j], \
                pix_average[j]
        continue
      print >>OutputCalibrationFileHandle, wav_bin_av[j], velocity_fit[j], velocity_err[j], \
            resolution_fit[j], resolution_err[j]

    OutputCalibrationFileHandle.close()
    # OutputResolutionFileHandle = open(OutputResolutionFile,'w')
    # for j in range(len(wav_bin_av)):
    #     print >>OutputResolutionFileHandle, wav_bin_av[j], resolution_fit[j], resolution_err[j] 
    # 
    # OutputResolutionFileHandle.close()
CalibrationLogFileHandle.close()
CalibrationSummaryFileHandle.close()
print "Finished calibration run. ", datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")