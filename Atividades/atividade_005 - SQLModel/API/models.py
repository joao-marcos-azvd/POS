# Aqui eu importo as biblioteca que vão ser utilizadas na definição dos modleos 
from sqlmodel import SQLModel, Field
from typing import Optional # Essa biblioteca aqui serve para quando eu quero ter campos opicionaid, que podem ser ou não respondidos.

# Definição do modelo pedido/tabela pedido
class Pedido(SQLModel, table=True):
    IdPedido: int = Field(primary_key=True)
    ProtocoloPedido: Optional[str] = None
    Esfera: Optional[str] = None
    UF: Optional[str] = None
    Municipio: Optional[str] = None
    OrgaoDestinatario: Optional[str] = None
    Situacao: Optional[str] = None
    DataRegistro: Optional[str] = None
    PrazoAtendimento: Optional[str] = None
    FoiProrrogado: Optional[str] = None
    FoiReencaminhado: Optional[str] = None
    FormaResposta: Optional[str] = None  
    OrigemSolicitacao: Optional[str] = None
    IdSolicitante: Optional[int] = None
    AssuntoPedido: Optional[str] = None
    SubAssuntoPedido: Optional[str] = None
    Tag: Optional[str] = None
    DataResposta: Optional[str] = None
    Decisao: Optional[str] = None
    EspecificacaoDecisao: Optional[str] = None