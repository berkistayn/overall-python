import win32gui
import win32ui
import win32con
import win32api
import sys


def take_screenshot(saved_img_path=r'C:\users\tosun\Desktop\screenshot.png',
                    app_class='AcrobatSDIWindow'):
    ### grab a handle to the main desktop window
    hdesktop = win32gui.GetDesktopWindow()
    hpdf = win32gui.FindWindow(app_class, None)
    
    ### To get the whole screen
    # width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    # height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    # left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    # top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    ### To get the desired app only
    left, top, right, bottom = win32gui.GetWindowRect(hpdf)
    width  = right - left
    height = bottom - top
    
    # create a device context
    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)
    
    # create a memory based device context
    mem_dc = img_dc.CreateCompatibleDC()
    
    # create a bitmap object
    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)
    
    # copy the screen into our memory device context
    mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top),win32con.SRCCOPY)
    
    # save the bitmap to a file
    screenshot.SaveBitmapFile(mem_dc, saved_img_path)
    # free our objects
    mem_dc.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())


def mark_on_img(img_path, mark_rect,
                d_block_marker = 5,
                d_marker = 4,
                d_outter = 50,
                d_outmost = 4):
    # mark the desired location on the screenshot
    try:
        from PIL import Image, ImageDraw, ImageColor
    except ModuleNotFoundError:
        print("You have to install 'PIL' in order to use the debug module.") # PIL OR Pillow
        return

    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    
    # update such that it does not interfere with rectangle

    mark_rect   = [point - (d_marker + d_block_marker) if counter < 2  else point + (d_marker + d_block_marker) 
                    for counter, point in enumerate(mark_rect)]
    outter_ring = [point - d_outter if counter < 2  else point + d_outter for counter, point 
                    in enumerate(mark_rect)]
    outmost_ring =[point - d_outmost if counter < 2  else point + d_outmost for counter, point 
                    in enumerate(outter_ring)]

    draw.rectangle(mark_rect,    width=d_marker,  outline=(0, 0, 255))
    draw.rectangle(outter_ring,  width=d_outter,  outline=(255, 255, 0))
    draw.rectangle(outmost_ring, width=d_outmost, outline=(0, 0, 255))
    
    img.save(img_path)


if __name__ == "__main__":
    img_path = r'C:\users\tosun\Desktop\screenshot.png'
    take_screenshot(img_path)
    mark_on_img(img_path, (300, 310, 320, 320))

