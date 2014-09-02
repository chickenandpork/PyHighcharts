from distutils.core import setup

	#https://docs.python.org/2.0/dist/creating-rpms.html

setup(name='PyHighcharts',
	version='1.0',
	description='A convenient wrapper for Highchart generation procedurally or on the command-line to browser output',
	long_description='A convenient wrapper for Highchart generation procedurally or on the command-line to browser output.\n\n'+
	'For documentation on highcharts visit: http://api.highcharts.com/highcharts (Highcharts API)\n\n'+
	'And remember Highcharts is only free for non-commercial use: Pop over to http://shop.highsoft.com/highcharts.html (Highcharts Licensing) for more info!',
	license='Free for Non-Commercial use',
	author='Findlay Yeates',
	author_email='fidyeates@exeter.ac.uk.unconfirmed',
	url='https://github.com/fidyeates/PyHighcharts',
	packages=['PyHighcharts','PyHighcharts.highcharts','PyHighcharts.highcharts.ref'],
	package_dir={'PyHighcharts': ''},
	)
