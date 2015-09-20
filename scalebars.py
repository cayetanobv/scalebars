# -*- coding: utf-8 -*-
#
#  Generating variable scalebars using USGS library variable_scalebar:
#  https://github.com/USGS-Astrogeology/variable_scalebar
#
#  Scalebars generated: Lambert Conformal Conic and Mercator.
#
#  Author: Cayetano Benavent, 2015.
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

from scalebar.bar import bar


def getScaleBar(wkt, ext, outputname, lat_tick_interval, fontsize):
    try:
        bar.ScaleBar.from_projstring(wkt, ext, outputname=outputname,
                                        lat_tick_interval=lat_tick_interval,
                                        fontsize=fontsize)
    except Exception as err:
        print("Error: {0}".format(err))

def main():
    wkt_01 = 'PROJCS["WGS 84 / Pseudo-Mercator",GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]],PROJECTION["Mercator_1SP"],PARAMETER["central_meridian",0],PARAMETER["scale_factor",1],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["metre",1,AUTHORITY["EPSG","9001"]],AXIS["X",EAST],AXIS["Y",NORTH],EXTENSION["PROJ4","+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +wktext  +no_defs"],AUTHORITY["EPSG","3857"]]'
    wkt_02 = 'PROJCS["ETRS89 / LCC Europe",GEOGCS["ETRS89",DATUM["European_Terrestrial_Reference_System_1989",SPHEROID["GRS 1980",6378137,298.257222101,AUTHORITY["EPSG","7019"]],TOWGS84[0,0,0,0,0,0,0],AUTHORITY["EPSG","6258"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4258"]],PROJECTION["Lambert_Conformal_Conic_2SP"],PARAMETER["standard_parallel_1",35],PARAMETER["standard_parallel_2",65],PARAMETER["latitude_of_origin",52],PARAMETER["central_meridian",10],PARAMETER["false_easting",4000000],PARAMETER["false_northing",2800000],UNIT["metre",1,AUTHORITY["EPSG","9001"]],AUTHORITY["EPSG","3034"]]'

    getScaleBar(wkt_01, ((0,0),(180,60)), '/tmp/merc_wkt.svg', 10, 14)
    getScaleBar(wkt_02, ((0,0),(180,60)), '/tmp/lcc_wkt.svg', 10, 14)

if __name__ == '__main__':
    main()
