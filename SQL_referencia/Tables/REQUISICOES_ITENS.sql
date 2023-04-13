/******************************************************************************/
/***               Generated by IBExpert 13/04/2023 17:14:04                ***/
/******************************************************************************/

/******************************************************************************/
/***      Following SET SQL DIALECT is just for the Database Comparer       ***/
/******************************************************************************/
SET SQL DIALECT 3;



/******************************************************************************/
/***                                 Tables                                 ***/
/******************************************************************************/



CREATE TABLE REQUISICOES_ITENS (
    ID_REQUISICAO   INTEGER NOT NULL,
    ID_ITEM         INTEGER NOT NULL,
    ID_PRODUTO      INTEGER,
    DESCRICAO       VARCHAR(60),
    QTDE            FLOAT,
    VALOR_UNITARIO  MOEDA /* MOEDA = DECIMAL(15,2) */,
    REF             VARCHAR(15),
    DADOS           BLOB SUB_TYPE 1 SEGMENT SIZE 80,
    CODIGO_FAB      VARCHAR(20),
    MARCA           VARCHAR(50),
    CODIGO_BARRA    VARCHAR(40),
    ENTREGAR        FLOAT,
    ENTREGUE        FLOAT,
    DATA_ENTREGA    DATE
);




/******************************************************************************/
/***                              Primary Keys                              ***/
/******************************************************************************/

ALTER TABLE REQUISICOES_ITENS ADD PRIMARY KEY (ID_REQUISICAO, ID_ITEM);


/******************************************************************************/
/***                                Indices                                 ***/
/******************************************************************************/

CREATE UNIQUE INDEX XPKREQUISICOES_ITENS ON REQUISICOES_ITENS (ID_REQUISICAO, ID_ITEM);


/******************************************************************************/
/***                               Privileges                               ***/
/******************************************************************************/
