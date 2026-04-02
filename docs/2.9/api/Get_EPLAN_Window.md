# How to display a MessageBox with the EPLAN window as owner

How to display a MessageBox with the EPLAN window as owner 

If you would like to display a message box or a modal dialog, which uses the EPLAN window as owner window, you can do this as in the following example:

C# |  Copy Code  
---|---  
      
    
    Process oCurrent = Process.GetCurrentProcess();
    var ww = new WindowWrapper(oCurrent.MainWindowHandle);
    MessageBox.Show(ww, "dialog with owner");
    MessageBox.Show("dialog without owner");
    public class WindowWrapper : System.Windows.Forms.IWin32Window
    {
     public WindowWrapper(IntPtr handle)
     {
     _hwnd = handle;
     }
     public IntPtr Handle
     {
     get { return _hwnd; }
     }
     private IntPtr _hwnd;
    }
