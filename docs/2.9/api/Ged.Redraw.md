# Ged.Redraw
Force a Redraw for the GED 

  


  
**Example**

```csharp
m_EventHandler = new EventHandler("Ged.Redraw");
m_EventHandler.EplanEvent += delegate {
    new Decider().Decide(EnumDecisionType.eOkDecision, "Ged.Redraw was called!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
};
```
