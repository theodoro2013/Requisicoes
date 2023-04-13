SET TERM ^ ;

create or alter procedure MOB_CADASTRAR_PEDIDO (
    USUARIO integer,
    CLIENTE integer,
    DATA varchar(10),
    HORA varchar(5),
    OBSERVACAO blob sub_type 1 segment size 80 character set WIN1252,
    PRAZO_PEDIDO blob sub_type 1 segment size 80 character set WIN1252,
    PAGAMENTO integer,
    VALOR_DESCONTO float,
    TOTAL_PEDIDO float,
    TIPO_OPERACAO integer,
    CONDICAO_PAGAMENTO integer)
as
declare variable CD_NP integer;
declare variable CD_PD integer;
declare variable CD_NPI integer;
declare variable CD_NTP integer;
declare variable CD_DPP integer;
declare variable CD_MOB integer;
declare variable PEMPRESA integer;
declare variable OP_DI smallint;
BEGIN
    PEMPRESA = 1;

    SELECT GEN_ID(PEDIDOS,1) FROM RDB$DATABASE INTO :CD_NP;

    SELECT MAX(NR_PED) FROM ADM_SEQUENCIA WHERE ID_EMPRESA = :PEMPRESA INTO :CD_PD;

    SELECT DESCONTO_ITEM FROM CONFIG WHERE ID_EMPRESA = :PEMPRESA INTO :OP_DI;

    IF (CD_PD IS NULL) THEN
        CD_PD = 1;
        ELSE
        CD_PD = CD_PD + 1;

    SELECT COALESCE(NR_MOB,0) FROM ADM_GLOBAL INTO :CD_MOB;

    CD_MOB = (CD_MOB + 1);

    UPDATE ADM_GLOBAL SET NR_MOB = :CD_MOB;

    INSERT INTO PEDIDOS (ID_PEDIDO, ID_MOBILE, PEDIDO, ID_CLIENTE, ID_ESPECIE, DATA_HORA, ID_FUNCIONARIO, ID_VENDEDOR,
            VALOR_PEDIDO, ID_NATUREZA, AJUSTE, TIPO, STATUS, ID_DEPTO, ID_PORTADOR, NOTA_FISCAL, CUPOM_FISCAL,
            BASE_CALCULO, VALOR_ICMS, BASE_ICMS_SUB, VALOR_ICMS_SUB, DESCONTO, VALOR_SERVICOS, VALOR_CUSTOS, VALOR_BASE,
            VALOR_ENTRADA, ITENS, QTDE_TOTAL, ID_FORMA, VALOR_FRETE, TIPO_FRETE, TIPO_TRANSPORTE,
            N_NOTA, OUTRAS_DESPESAS, VALOR_IPI, NF, TIPO_PO, TIPO_A_PRECO, DEVOLUCAO, ENTREGA, TIPO_NOTA, TIPO_EMISSAO, 
            ACRESCIMO, PESO_TOTAL, OBS,STATUS_ENTREGA)
    VALUES ( :CD_NP, 1, 'MOB'||:CD_MOB, :CLIENTE, :PAGAMENTO, CURRENT_TIMESTAMP, :USUARIO, :USUARIO,
    (:TOTAL_PEDIDO+:VALOR_DESCONTO),:TIPO_OPERACAO,0, 1, 1,
    (SELECT DEPTO_PADRAO FROM CONFIG WHERE ID_EMPRESA = :PEMPRESA),
    (SELECT PORTADOR_PADRAO FROM CONFIG WHERE ID_EMPRESA = :PEMPRESA),
    '0', '0',0, 0, 0, 0,((:VALOR_DESCONTO*100)/ ( 
    CASE WHEN 
        (:TOTAL_PEDIDO+:VALOR_DESCONTO) = 0 THEN 1 
    ELSE (:TOTAL_PEDIDO+:VALOR_DESCONTO)END )), 0, 0, 0, 0, 0, 0, 
    :CONDICAO_PAGAMENTO, 0, 2, 1,0, 0, 0, 2, 1, 0, 0, 0, 1, 0, 0, 0, :OBSERVACAO,1);


    EXECUTE STATEMENT 'SET GENERATOR PEDIDOS TO ' || :CD_NP;

    -- ID_PEDIDO = :CD_NP;

END^

SET TERM ; ^

/* Following GRANT statetements are generated automatically */

GRANT SELECT ON ADM_SEQUENCIA TO PROCEDURE MOB_CADASTRAR_PEDIDO;
GRANT SELECT ON CONFIG TO PROCEDURE MOB_CADASTRAR_PEDIDO;
GRANT SELECT,UPDATE ON ADM_GLOBAL TO PROCEDURE MOB_CADASTRAR_PEDIDO;
GRANT INSERT ON PEDIDOS TO PROCEDURE MOB_CADASTRAR_PEDIDO;

/* Existing privileges on this procedure */

GRANT EXECUTE ON PROCEDURE MOB_CADASTRAR_PEDIDO TO SYSDBA;