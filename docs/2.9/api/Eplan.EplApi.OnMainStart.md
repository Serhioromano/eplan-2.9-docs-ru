# Eplan.EplApi.OnMainStart
Send when the Main Start is done. This is when a mainframe is available. The event is not send when the application is started in offline modus or to execute an action. 

  


#### Parameters

Has no event parameter.  


  
**Example**

```csharp
m_EventHandler = new EventHandler("Eplan.EplApi.OnMainStart");
m_EventHandler.EplanEvent += delegate {
    new Decider().Decide(EnumDecisionType.eOkDecision, "On main start was called!", "OnMainStart", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
};
```
