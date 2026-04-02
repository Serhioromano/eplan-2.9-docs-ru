# Page.ConnectionDirty
Event when a Page gets dirty 

  


  
**Example**

```csharp
m_EventHandler = new EventHandler("Page.ConnectionDirty");
m_EventHandler.EplanEvent += delegate {
    new Decider().Decide(EnumDecisionType.eOkDecision, "Page.ConnectionDirty was called!", "Title", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
};
```
