set timezone to 'GMT';
    Select
              t1."Id" as id
             ,t1."Finance_Reporting_Name" as name
             ,coalesce(t1."Sales_Territory",'Other') as country
             ,case when t1."IsWon"='true' then 1 else 0 end is_won
             ,st."StageName"
             ,st."ARR"*er.rate arr_est
             ,t1."ARR" arr_now
             ,hl.dt as date
             ,st."CloseDate"
             ,left(cast(t1."CloseDate" as varchar),10) as actual_Closed
             ,t1."source"
             ,t1."StageName" current_stage
    from "public"."SALESFORCE_REPORTS_opportunities_enriched" t1
                inner join 
                "public"."SALESFORCE_REPORTS_exchange_rate" er
                on t1.currency=er.from
                and er.month is not null
                and er.to='USD'
                and er."Exchange Rate Date"=(date_trunc('month',t1."CloseDate"::date)-interval '1 day')
                and t1."date"=(select max(date) from "public"."SALESFORCE_REPORTS_opportunities_enriched")
                and t1."IsClosed"='true'
                and t1."Type" like 'Initial%'
                and t1."Id"<>''
                inner join
                    (
                    select
                    "Id" id
                    ,"Type" typ
                    ,"StageName"
                    ,min(date) dt
                    from "public"."SALESFORCE_REPORTS_opportunities_enriched"
                    where "StageName" in 
                    ('Sales Accepted Lead',
                    'Goal',
                    'Champion',
                    'Evaluation',
                    'Written Agreement',
                    'Proposal')
                    and "Type" like 'Initial%'
                    group by 1,2,3
                    ) hl
                on t1."Id"=hl.id
                and t1."Type"=hl.typ
                left join 
                    "public"."SALESFORCE_REPORTS_opportunities_enriched" st
                    on st."Id"=hl.id
                    and st."Type"=hl.typ
                    and st.date=hl.dt
                    order by name, date
