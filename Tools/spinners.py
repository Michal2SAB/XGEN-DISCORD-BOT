from cairosvg import svg2png
from PIL import Image, ImageDraw, ImageFont

def SvgToPng(HexOne1, HexOne2, HexTwo1, HexTwo2, spinner):
  try:
    outer_fill = ""
    inner_fill = ""
      
    if spinner == 'oldskool':
      outer_fill = """
<svg xmlns:xlink="http://www.w3.org/1999/xlink" height="70.0px" width="70.0px" xmlns="http://www.w3.org/2000/svg">
  <g transform="matrix(1, 0, 0, 1, 35.0, 35.0)">
    <path d="M31.0 -8.3 Q31.95 -4.35 32.0 0.0 31.95 4.3 31.0 8.25 M-31.0 8.3 Q-32.0 4.35 -32.0 0.0 -32.0 -4.4 -31.0 -8.4 M-8.3 -31.0 Q-4.4 -32.05 0.0 -32.0 4.35 -32.05 8.3 -31.0 M8.3 30.95 Q4.35 31.95 0.0 32.0 L-8.25 31.0" fill="none" stroke="{}" stroke-opacity="0.75" stroke-linecap="round" stroke-linejoin="round" stroke-width="6.0"/>
    <path d="M31.0 -8.3 Q31.95 -4.35 32.0 0.0 31.95 4.3 31.0 8.25 M-31.0 8.3 Q-32.0 4.35 -32.0 0.0 -32.0 -4.4 -31.0 -8.4 M-8.3 -31.0 Q-4.4 -32.05 0.0 -32.0 4.35 -32.05 8.3 -31.0 M8.3 30.95 Q4.35 31.95 0.0 32.0 L-8.25 31.0" fill="none" stroke="{}" stroke-opacity="0.75" stroke-linecap="round" stroke-linejoin="round" stroke-width="3.0"/>
  </g>
</svg>
""".format(HexOne1, HexOne2)

      inner_fill = """
<svg xmlns:xlink="http://www.w3.org/1999/xlink" height="54.0px" width="54.0px" xmlns="http://www.w3.org/2000/svg">
  <g transform="matrix(1, 0, 0, 1, 27.0, 27.0)">
    <path d="M23.25 -6.25 Q24.0 -3.3 24.0 0.0 24.0 3.2 23.25 6.1 M-23.25 6.2 Q-24.0 3.25 -24.0 0.0 -24.0 -3.35 -23.25 -6.35 M-6.2 -23.25 L0.0 -24.0 6.25 -23.25 M6.25 23.2 L0.0 24.0 -6.2 23.2" fill="none" stroke="{}" stroke-opacity="0.75" stroke-linecap="round" stroke-linejoin="round" stroke-width="6.0"/>
    <path d="M23.25 -6.25 Q24.0 -3.3 24.0 0.0 24.0 3.2 23.25 6.1 M-23.25 6.2 Q-24.0 3.25 -24.0 0.0 -24.0 -3.35 -23.25 -6.35 M-6.2 -23.25 L0.0 -24.0 6.25 -23.25 M6.25 23.2 L0.0 24.0 -6.2 23.2" fill="none" stroke="{}" stroke-opacity="0.75" stroke-linecap="round" stroke-linejoin="round" stroke-width="3.0"/>
  </g>
</svg>
""".format(HexTwo1, HexTwo2)
      
    elif spinner == 'pro':
      outer_fill = """
<svg xmlns:xlink="http://www.w3.org/1999/xlink" height="72.0px" width="72.0px" xmlns="http://www.w3.org/2000/svg">
  <g transform="matrix(1, 0, 0, 1, 36.0, 35.8)">
    <path d="M-8.3 -30.8 Q-4.4 -31.85 0.0 -31.8 4.35 -31.85 8.3 -30.8 M-31.0 8.5 Q-32.0 4.55 -32.0 0.2 -32.0 -4.2 -31.0 -8.2 M31.0 -8.1 Q31.95 -4.15 32.0 0.2 31.95 4.5 31.0 8.45 M8.3 31.15 Q4.35 32.15 0.0 32.2 L-8.25 31.2" fill="none" stroke="{}" stroke-opacity="0.75" stroke-linecap="square" stroke-linejoin="round" stroke-width="6.0"/>
  </g>
</svg>
""".format(HexOne1)

      inner_fill = """
<svg xmlns:xlink="http://www.w3.org/1999/xlink" height="56.0px" width="56.0px" xmlns="http://www.w3.org/2000/svg">
  <g transform="matrix(1, 0, 0, 1, 28.0, 28.0)">
    <path d="M23.25 -6.25 Q24.0 -3.3 24.0 0.0 24.0 3.2 23.25 6.1 M-6.2 -23.25 L0.0 -24.0 6.25 -23.25 M-23.25 6.2 Q-24.0 3.25 -24.0 0.0 -24.0 -3.35 -23.25 -6.35 M6.25 23.2 L0.0 24.0 -6.2 23.2" fill="none" stroke="{}" stroke-opacity="0.75" stroke-linecap="square" stroke-linejoin="round" stroke-width="6.0"/>
  </g>
</svg>
""".format(HexTwo1)
      
    elif spinner == 'wreath':
      outer_fill = """
<svg xmlns:xlink="http://www.w3.org/1999/xlink" height="415.7px" width="416.25px" xmlns="http://www.w3.org/2000/svg">
  <g transform="matrix(1, 0, 0, 1, 230.35, 219.95)">
    <path d="M155.0 -101.65 L151.95 -104.85 153.95 -109.8 158.85 -106.15 157.55 -100.2 162.45 -102.3 170.95 -88.4 168.55 -87.15 168.4 -84.7 162.95 -83.45 159.1 -92.95 153.25 -90.8 147.25 -96.0 155.0 -101.65 M107.6 -135.7 L109.65 -127.65 119.9 -124.75 112.4 -116.55 113.9 -109.8 107.5 -113.45 108.55 -117.55 102.95 -118.1 96.5 -129.15 101.1 -135.4 107.6 -135.7 M92.85 -167.35 L83.55 -170.75 79.7 -175.95 89.85 -182.45 93.1 -178.75 91.2 -175.3 96.5 -170.9 92.85 -167.35 M37.55 -208.1 L32.05 -219.95 38.0 -218.0 42.25 -219.6 46.15 -209.45 37.55 -208.1 M185.65 -26.3 L179.45 -20.2 173.25 -20.6 172.0 -25.0 176.95 -30.5 165.0 -29.2 163.1 -32.65 171.1 -40.05 170.05 -45.9 176.7 -43.35 175.45 -36.3 180.0 -39.1 185.9 -29.0 185.65 -26.3 M-172.7 118.8 L-178.75 122.4 -176.4 130.75 -183.4 126.9 -183.25 121.3 -190.15 121.8 Q-191.55 121.85 -192.8 121.25 -195.8 119.65 -197.6 116.5 L-194.1 105.7 -189.3 105.9 -188.7 115.8 -175.1 113.95 -172.7 118.8 M-216.3 44.15 L-209.8 43.85 -207.75 51.9 -197.5 54.8 -205.0 63.0 -203.5 69.75 -209.9 66.1 -208.85 62.0 -214.45 61.45 -220.9 50.4 -216.3 44.15 M-22.85 195.7 Q-26.6 196.0 -29.65 194.0 L-34.0 184.0 -24.0 183.0 -22.25 174.85 -20.4 173.05 -16.6 173.3 -13.0 181.2 -7.85 179.9 -4.3 182.9 -10.6 188.1 -14.75 185.45 -14.6 191.7 Q-17.8 195.55 -22.85 195.7 M-86.35 169.25 L-86.35 158.95 -72.2 158.95 -72.2 169.25 -86.35 169.25 M-137.8 177.8 L-137.8 167.9 -127.8 167.9 -127.8 177.8 -137.8 177.8 M-146.0 -183.0 L-135.35 -189.75 -126.5 -181.6 -134.5 -177.35 -134.75 -165.9 -137.65 -162.7 -142.0 -163.0 -146.0 -183.0 M-206.15 -1.8 L-210.0 -7.0 -199.85 -13.5 -196.6 -9.8 -198.5 -6.35 -193.2 -1.95 -196.85 1.6 -206.15 -1.8 M-219.7 -52.25 L-230.35 -52.25 -230.35 -63.0 -219.7 -63.0 -219.7 -52.25 M-191.55 -160.15 L-188.45 -152.1 -198.95 -147.75 -205.9 -138.5 -212.5 -138.6 -213.0 -143.0 -207.05 -155.45 -191.55 -160.15 M-11.55 -199.8 L-4.45 -198.3 -0.25 -190.1 -0.7 -187.05 -7.9 -188.65 -9.95 -184.45 -14.6 -182.45 -15.8 -197.35 -13.5 -194.5 -11.55 -199.8 M-67.5 -211.75 L-61.35 -204.25 -71.45 -187.55 -77.05 -188.5 -82.0 -209.0 -67.5 -211.75 M85.9 114.1 L90.7 114.3 91.3 124.2 104.9 122.35 107.3 127.2 101.25 130.8 103.6 139.15 96.6 135.3 96.75 129.7 89.85 130.2 87.2 129.65 Q84.2 128.05 82.4 124.9 L85.9 114.1 M132.2 114.1 L142.2 114.1 142.2 124.0 132.2 124.0 132.2 114.1 M39.45 186.2 L32.25 180.85 32.05 178.75 39.1 174.3 43.35 176.15 Q42.25 172.3 43.7 168.5 45.6 163.7 50.5 161.7 L54.3 169.25 60.9 166.7 60.05 173.05 51.85 173.15 51.25 179.95 39.45 186.2 M168.8 74.9 L175.7 73.9 178.55 71.45 Q180.35 83.05 168.55 83.85 L168.8 74.9 M165.85 25.9 L163.7 34.5 153.8 35.2 155.0 27.5 151.1 24.3 Q152.6 23.2 154.3 22.4 159.8 19.9 165.75 21.75 L162.55 24.0 165.85 25.9" fill="{}" fill-opacity="0.75" fill-rule="evenodd" stroke="none"/>
""".format(HexOne1)
      
      inner_fill = """
<svg xmlns:xlink="http://www.w3.org/1999/xlink" height="465.4px" width="462.6px" xmlns="http://www.w3.org/2000/svg">
  <g transform="matrix(1, 0, 0, 1, 244.75, 243.8)">
    <path d="M45.3 -186.8 L57.55 -189.45 59.3 -188.75 63.05 -176.0 87.6 -165.3 Q92.15 -162.0 97.85 -159.35 104.45 -156.25 116.05 -147.8 L115.05 -135.45 134.2 -133.85 134.95 -133.25 139.25 -118.0 127.65 -107.0 140.85 -63.6 144.45 -65.45 153.05 -56.5 150.65 -51.4 157.85 -21.6 148.05 -29.2 147.45 -17.25 131.8 -17.7 115.3 5.3 108.55 -19.7 123.3 -50.7 110.05 -51.95 91.55 -41.95 90.55 -52.95 105.3 -72.7 89.55 -127.7 58.3 -133.7 46.05 -156.95 66.25 -156.4 59.25 -175.4 44.25 -185.4 45.3 -186.8 M146.3 -66.45 L154.25 -70.6 156.25 -84.8 163.9 -75.0 164.35 -66.7 157.05 -65.2 156.6 -64.2 146.3 -66.45 M147.35 -15.85 L146.65 -2.2 129.7 18.1 128.3 -0.95 147.35 -15.85 M141.1 27.05 L142.45 26.8 158.05 34.2 126.25 64.2 122.85 89.0 138.2 86.2 137.7 87.6 Q135.15 95.3 134.05 97.4 132.7 100.0 131.7 102.6 130.75 103.85 128.8 105.4 125.6 107.85 119.7 110.95 L90.8 124.05 Q81.85 128.0 75.6 131.1 L74.4 131.7 Q69.9 134.0 66.9 135.8 L64.95 137.05 58.85 135.0 32.4 150.8 33.3 147.05 23.3 143.8 11.25 155.7 -21.75 161.2 -13.95 148.6 -40.95 149.0 -40.6 141.6 -26.7 144.8 -40.7 119.05 -23.45 113.05 10.05 127.05 12.3 116.05 -0.95 96.05 93.05 103.55 102.3 91.55 Q88.05 89.55 87.8 76.05 L100.05 58.05 123.55 60.3 141.8 30.05 141.1 27.05 M31.05 156.45 L37.8 168.7 28.05 168.8 31.05 156.45 M-66.65 144.05 L-64.95 147.2 -74.15 155.6 -83.55 138.6 -92.55 136.4 -96.1 131.4 -83.95 132.8 -71.7 144.8 -66.65 144.05 M-99.5 126.6 L-101.95 123.2 -126.95 118.6 -122.75 130.8 Q-130.75 124.65 -138.3 117.65 L-138.15 108.0 -163.15 88.2 -164.05 89.65 -172.0 79.05 -169.35 72.4 -178.45 46.15 -176.9 45.6 -173.35 49.6 -170.75 20.6 -150.75 2.6 -148.4 -10.55 -146.45 -9.45 -128.95 -17.95 Q-155.95 39.05 -136.2 79.05 L-125.7 61.3 -109.45 88.55 -112.95 104.3 -99.5 126.6 M-148.7 -10.7 L-171.75 -5.4 -187.45 -10.25 -188.15 -10.9 -172.35 -23.4 -171.75 -32.6 -159.15 -44.6 -159.0 -53.6 -144.45 -65.95 -141.45 -43.45 -157.95 -15.95 -148.7 -10.7 M-158.9 -60.15 L-158.75 -72.8 -177.75 -67.4 -188.35 -52.0 -189.5 -53.1 -189.45 -53.2 -188.4 -66.1 -179.15 -70.2 -165.5 -90.45 -163.95 -82.2 -174.45 -70.45 -163.2 -73.2 -156.7 -86.7 -158.2 -61.2 -158.9 -60.15 M-161.65 -96.2 L-160.75 -97.6 -167.25 -100.75 -162.35 -116.15 Q-161.65 -118.2 -161.6 -125.8 L-159.9 -131.7 -153.6 -138.95 -145.75 -133.6 -137.75 -137.2 -126.75 -131.4 -98.15 -152.4 -104.55 -165.6 -116.3 -166.05 -107.95 -173.95 -92.1 -170.5 -85.15 -163.8 -53.35 -177.0 -61.95 -165.8 -32.15 -167.4 -9.95 -145.8 -6.55 -145.45 -1.45 -127.45 Q-61.95 -162.2 -86.2 -129.45 L-109.7 -111.7 -135.45 -115.2 -138.45 -126.2 -148.45 -116.2 -150.45 -105.45 -161.65 -96.2 M3.8 -152.5 L3.05 -166.0 -5.35 -173.4 1.85 -183.95 2.65 -184.3 34.65 -159.25 34.3 -157.2 44.3 -153.2 47.3 -140.45 26.55 -137.95 4.55 -152.7 3.8 -152.5" fill="{}" fill-rule="evenodd" stroke="none"/>
    <path d="M20.6 -230.9 L27.1 -232.95 29.15 -233.35 Q46.5 -231.65 59.25 -219.45 L62.25 -216.4 74.45 -222.4 103.45 -189.0 106.85 -196.8 120.85 -201.8 159.05 -158.0 154.85 -150.8 156.65 -139.4 180.05 -123.6 194.65 -91.2 188.05 -69.8 193.45 -62.4 202.25 -66.8 213.85 -57.4 207.25 -30.4 192.05 -33.4 217.85 4.8 207.65 31.8 183.85 19.4 203.85 62.4 199.45 78.6 179.65 92.6 168.45 123.2 147.25 130.2 155.85 136.0 157.25 149.4 138.65 167.4 128.65 167.2 110.85 187.6 96.25 179.4 80.25 194.2 66.25 193.4 46.65 209.8 23.65 195.4 15.05 200.4 20.25 207.6 7.25 221.6 -18.55 211.0 -18.15 195.6 -32.15 211.2 -54.75 217.8 -82.75 204.6 -66.95 185.4 -113.35 197.0 -129.75 190.6 -138.35 172.4 -150.35 172.8 -191.15 148.2 -190.75 134.6 -208.95 116.0 -205.55 92.6 -212.15 86.2 -219.95 91.2 -233.55 82.0 -230.75 53.6 -214.95 53.2 -244.75 15.6 -240.15 -5.8 -222.55 -1.8 -218.35 8.0 -215.15 0.0 -242.35 -41.8 -228.35 -83.0 -196.55 -109.75 Q-195.8 -111.8 -195.8 -112.4 L-196.0 -114.6 -205.55 -119.4 -195.75 -168.4 -133.95 -212.0 -104.95 -208.6 -108.75 -220.4 -100.75 -236.4 -74.55 -233.2 -69.35 -212.6 -39.55 -243.8 -6.75 -239.4 -8.75 -211.2 Q3.85 -224.3 20.6 -230.9 M59.3 -188.75 L55.25 -202.4 46.45 -203.6 50.45 -194.0 45.3 -186.8 44.25 -185.4 59.25 -175.4 66.25 -156.4 46.05 -156.95 37.25 -157.2 34.65 -159.25 2.65 -184.3 2.25 -184.6 1.85 -183.95 -5.35 -173.4 3.05 -166.0 3.8 -152.5 4.25 -144.4 -6.55 -145.45 -9.95 -145.8 -32.15 -167.4 -61.95 -165.8 -53.35 -177.0 -85.15 -163.8 -92.1 -170.5 -105.35 -183.2 -119.95 -166.2 -116.3 -166.05 -104.55 -165.6 -98.15 -152.4 -126.75 -131.4 -137.75 -137.2 -145.75 -133.6 -153.6 -138.95 -157.15 -141.4 -159.9 -131.7 -161.6 -125.8 Q-161.65 -118.2 -162.35 -116.15 L-167.25 -100.75 -160.75 -97.6 -161.65 -96.2 -165.5 -90.45 -179.15 -70.2 -188.4 -66.1 -207.95 -57.4 -195.15 -58.4 -189.5 -53.1 -188.35 -52.0 -177.75 -67.4 -158.75 -72.8 -158.9 -60.15 -159.0 -53.6 -159.15 -44.6 -171.75 -32.6 -172.35 -23.4 -188.15 -10.9 -188.55 -10.6 -187.45 -10.25 -171.75 -5.4 -148.7 -10.7 -148.35 -10.8 -148.4 -10.55 -150.75 2.6 -170.75 20.6 -173.35 49.6 -176.9 45.6 -179.75 42.4 -178.45 46.15 -169.35 72.4 -172.0 79.05 -174.35 84.8 -187.75 91.4 -172.55 103.6 -164.05 89.65 -163.15 88.2 -138.15 108.0 -138.3 117.65 -138.55 129.2 -130.75 134.6 -128.55 159.6 -119.55 140.2 -122.75 130.8 -126.95 118.6 -101.95 123.2 -99.5 126.6 -96.1 131.4 -92.55 136.4 -83.55 138.6 -74.15 155.6 -64.95 147.2 -66.65 144.05 -69.95 138.0 -65.75 119.6 -40.55 140.4 -40.6 141.6 -40.95 149.0 -13.95 148.6 -21.75 161.2 11.25 155.7 11.65 155.6 25.85 177.8 39.05 171.0 37.8 168.7 31.05 156.45 29.05 152.8 32.4 150.8 58.85 135.0 64.95 137.05 66.9 135.8 Q69.9 134.0 74.4 131.7 L75.6 131.1 Q81.85 128.0 90.8 124.05 L119.7 110.95 Q125.6 107.85 128.8 105.4 130.75 103.85 131.7 102.6 132.7 100.0 134.05 97.4 135.15 95.3 137.7 87.6 L138.2 86.2 122.85 89.0 126.25 64.2 158.05 34.2 142.45 26.8 141.1 27.05 119.25 30.6 129.7 18.1 146.65 -2.2 147.35 -15.85 147.45 -17.25 148.05 -29.2 157.85 -21.6 150.65 -51.4 153.05 -56.5 156.6 -64.2 157.05 -65.2 164.35 -66.7 169.45 -67.8 163.9 -75.0 156.25 -84.8 154.25 -70.6 146.3 -66.45 144.45 -65.45 140.85 -63.6 127.65 -107.0 139.25 -118.0 134.95 -133.25 134.2 -133.85 126.5 -139.95 116.05 -147.8 Q104.45 -156.25 97.85 -159.35 92.15 -162.0 87.6 -165.3 L63.05 -176.0 59.3 -188.75" fill="{}" fill-rule="evenodd" stroke="none"/>
""".format(HexTwo1, HexTwo2)

    svg2png(bytestring=outer_fill,write_to='outer.png')
    svg2png(bytestring=inner_fill,write_to='inner.png')
      
    return 'outer.png;inner.png'
  
  except Exception as e:
    print(e)

def gen(RGB1, RGB2, spinner):
  try:
    red0 = int(RGB1[:3])
    green0 = int(RGB1[3:][:3])
    blue0 = int(RGB1[6:][:3])

    red1 = int(RGB2[:3])
    green1 = int(RGB2[3:][:3])
    blue1 = int(RGB2[6:][:3])

    correctRed = red0
    correctGreen = green0
    correctBlue = blue0

    if red0 < 0:
      correctRed = 0

    if green0 < 0:
      correctGreen = 0

    if blue0 < 0:
      correctBlue = 0

    HexOne1 = '#%02x%02x%02x' % (correctRed, correctGreen, correctBlue)

    finalred0 = 0
    finalgreen0 = 0
    finalblue0 = 0

    if red0 > 153:
      finalred0 = 255
    else:
      finalred0 = red0 + 102
      
    if green0 > 153:
      finalgreen0 = 255
    else:
      finalgreen0 = green0 + 102
      
    if blue0 > 153:
      finalblue0 = 255
    else:
      finalblue0 = blue0 + 102
      
    HexOne2 = '#%02x%02x%02x' % (finalred0, finalgreen0, finalblue0)


    correctRed1 = red1
    correctGreen1 = green1
    correctBlue1 = blue1

    if red1 < 0:
      correctRed1 = 0

    if green1 < 0:
      correctGreen1 = 0

    if blue1 < 0:
      correctBlue1 = 0

    HexTwo1 = '#%02x%02x%02x' % (correctRed1, correctGreen1, correctBlue1)

    finalred1 = 0
    finalgreen1 = 0
    finalblue1 = 0
    
    if spinner == 'wreath':
      if red1 > 204:
        finalred1 = 255
      else:
        finalred1 = red1 + 51
      
      if green1 > 204:
        finalgreen1 = 255
      else:
        finalgreen1 = green1 + 51
      
      if blue1 > 204:
        finalblue1 = 255
      else:
        finalblue1 = blue1 + 51
        
    else:
      if red1 > 51:
        finalred1 = 255
      else:
        finalred1 = red1 + 204
      
      if green1 > 51:
        finalgreen1 = 255
      else:
        finalgreen1 = green1 + 204
      
      if blue1 > 51:
        finalblue1 = 255
      else:
        finalblue1 = blue1 + 204
      
    HexTwo2 = '#%02x%02x%02x' % (finalred1, finalgreen1, finalblue1)

    theImage1, theImage2 = SvgToPng(HexOne1, HexOne2, HexTwo1, HexTwo2, spinner).split(';')
      
      
    outer = Image.open(theImage1)
    back_outer = outer.copy()
      
    inner = Image.open(theImage2)
      
    back_outer.paste(inner, (8, 9))
    back_outer.save('spinner.png')
    
    return 'spinner.png'
      
  except Exception as e:
    print(e)