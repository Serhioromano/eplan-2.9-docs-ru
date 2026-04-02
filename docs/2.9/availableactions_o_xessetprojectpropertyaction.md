# Операция: XEsSetProjectPropertyAction

**Параметр** |  **Описание**
---|---
PropertyId  |  Идентификатор определяемого свойства (= номер свойства)
PropertyIdentName  |  Идентификатор определенного пользователем свойства, в том виде, в котором он был задан пользователем
PropertyIndex  |  Индекс свойства (в большинстве случаев — 0)
PropertyValue  |  Новое значение свойства

!!! example "Пример:"

    XEsSetProjectPropertyAction
    /PropertyId:?
    /PropertyIdentName:PEP.Project.PVW_1
    /PropertyIndex:0
    /PropertyValue:"?"
