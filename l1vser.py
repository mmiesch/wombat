
"""
This is used to compare in situ SW time series from Enlil at two different locations.  The original intent was to compare the time series at Earth and at L1.
"""

import netCDF4 as nc
import seaborn as sns
import matplotlib.pyplot as plt

dt = 1.0 / (3600.0*24.0)

#------------------------------------------------------------------------------
file1 = 'wsa_enlil.t13z.l1/wsa_enlil.t13z.suball.nc'
ds1 = nc.Dataset(file1)

time1 = ds1['Earth_TIME'][:] * dt
rho1  = ds1['Earth_Density'][:]
T1    = ds1['Earth_Temperature'][:]
x1    = ds1['Earth_X1'][:]
y1    = ds1['Earth_X2'][:]
z1    = ds1['Earth_X3'][:]
vx1   = ds1['Earth_V1'][:] * 1.e-3
vy1   = ds1['Earth_V2'][:] * 1.e-3
vz1   = ds1['Earth_V3'][:] * 1.e-3
bx1   = ds1['Earth_B1'][:]
by1   = ds1['Earth_B2'][:]
bz1   = ds1['Earth_B3'][:]
bp1   = ds1['Earth_BP_POLARITY'][:]

#------------------------------------------------------------------------------
file2 = 'wsa_enlil.t13z.earth/wsa_enlil.t13z.suball.nc'
ds2 = nc.Dataset(file2)

time2 = ds2['Earth_TIME'][:] * dt
rho2  = ds2['Earth_Density'][:]
T2    = ds2['Earth_Temperature'][:]
x2    = ds2['Earth_X1'][:]
y2    = ds2['Earth_X2'][:]
z2    = ds2['Earth_X3'][:]
vx2   = ds2['Earth_V1'][:] * 1.e-3
vy2   = ds2['Earth_V2'][:] * 1.e-3
vz2   = ds2['Earth_V3'][:] * 1.e-3
bx2   = ds2['Earth_B1'][:]
by2   = ds2['Earth_B2'][:]
bz2   = ds2['Earth_B3'][:]
bp2   = ds2['Earth_BP_POLARITY'][:]

print(f"length1 {len(time1)}")
print(f"length2 {len(time2)}")

#------------------------------------------------------------------------------

fig = plt.figure(figsize = (16,12))
#fig, ax = plt.subplots(nrows = 2, ncols = 1, sharex=True, figsize = (16,12))

Tcolor = '#7F5217'
lw = 3

xrange = (-0.5, 5.0)

sns.set_theme(style={'axes.facecolor': '#FFF8DC'}, palette='colorblind')

#------------

ax1 = fig.add_subplot(2,1,1)
sns.lineplot(x = time1, y = rho1, color='b', linewidth = lw, ax = ax1)
sns.lineplot(x = time2, y = rho2, color=Tcolor, linewidth = lw, ax = ax1)

ax1.fill_between(x = time1, y1 = rho1, y2 = rho2, color='b', alpha = 0.3)

ax1.set_ylim((0.25e-20,1.75e-20))
ax1.set_ylabel('Density (g cm$^{-3}$)', fontweight = 'bold')

ax1.set_xlim(xrange)

#------------

ax2 = fig.add_subplot(2,1,2)
sns.lineplot(x = time1, y = vx1, color='b', linewidth = lw, ax = ax2)
sns.lineplot(x = time2, y = vx2, color=Tcolor, linewidth = lw, ax = ax2)

ax2.fill_between(x = time1, y1 = vx1, y2 = vx2, color='b', alpha = 0.3)

ax2.set_ylim((300,600))
ax2.set_ylabel('Velocity (km s$^{-1}$)', fontweight = 'bold')

ax2.set_xlim(xrange)
ax2.set_xlabel('time (days)', fontweight = 'bold')

#------------
fig.tight_layout(pad=1,rect=(0.01,0.01,.99,.98))

plt.show()