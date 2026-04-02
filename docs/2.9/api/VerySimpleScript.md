# Structure of a simple script

A script consists of a at least one public class with at least one public function. This function needs to be marked with the attribute [Start].

The following example shows a very simple script.

=== "CS"

    ```
    public class VerySimpleScript
    {
         [Start]
         public void MyFunction()
         {
               new Decider().Decide(EnumDecisionType.eOkDecision, "MyFunction was called!", "VerySimpleScript", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
               return;
         }
    }
    ```

=== "VB"

    ```vb
     Public Class VerySimpleScript
       <Start> _
        Public Sub MyFunction()
          Dim dec As Decider = New Decider
          dec.Decide(EnumDecisionType.eOkDecision, "MyFunction was called!", "VerySimpleScript", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK)
          Return
       End Sub 'MyFunction
     End Class 'VerySimpleScript
    ```

In this example the class "VerySimpleScript" with a function "MyFunction" was created. The function was marked by the attribute "[Start]". 

When this script is run, using the menu point "[Scripts](Scripts.html)>Run..." the function "MyFunction" and a message box appears: 

![This message boy appears, when you run the very simple script.](VerySimpleScript.png)

A script may contain more than one function. There even can be several classes in a script. However there only may be exactly one function marked by the "[Start]" attribute!
