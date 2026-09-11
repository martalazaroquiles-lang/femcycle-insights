-- Calculate phase date ranges per cycle, based on actual Cycle Length 
-- and Period Length for each row (not fixed 28-day assumptions).
-- Luteal phase = fixed ~14 days before the next cycle starts (standard 
-- across most cycle lengths, per clinical literature).
-- Follicular phase = everything between the end of menstruation and 
-- the start of ovulation (variable length, absorbs cycle length differences).

SELECT
    "User ID",
    "Cycle Start Date",
    "Cycle Length",
    "Period Length",
    
    -- Menstrual phase: day 1 to Period Length
    "Cycle Start Date" AS menstrual_start,
    date("Cycle Start Date", '+' || ("Period Length" - 1) || ' days') AS menstrual_end,
    
    -- Follicular phase: right after menstruation ends, until ovulation starts
    date("Cycle Start Date", '+' || "Period Length" || ' days') AS follicular_start,
    date("Cycle Start Date", '+' || ("Cycle Length" - 15) || ' days') AS follicular_end,
    
    -- Ovulation: a short window, ~14 days before next cycle
    date("Cycle Start Date", '+' || ("Cycle Length" - 14) || ' days') AS ovulation_day,
    
    -- Luteal phase: last 13 days before next cycle
    date("Cycle Start Date", '+' || ("Cycle Length" - 13) || ' days') AS luteal_start,
    date("Cycle Start Date", '+' || ("Cycle Length" - 1) || ' days') AS luteal_end

FROM ciclos;