local http = require("socket.http")

function handlePu(s)
    -- local inner = s:sub(5, -2) -- strip off \pu{ and }
    local body, code, headers, status = http.request("https://mhchem-api.vercel.app/parseTex?tex=" .. s)
    -- print(code, status, #body)
    local result = body
    if not result then
        io.stderr:write("Could not parse mhchem formula " .. inner .. "\n")
        return "\\text{Could not parse}"
    end
    return result
end

function RawInline(el)
    if (el.format == "latex" or el.format == "tex") and el.text:match("\\pu{") then
        local result = handlePu(el.text)
        if result then
            return pandoc.Math("InlineMath", handlePu(el.text))
        end
    end
end

function RawBlock(el)
    local il = RawInline(el)
    if il then
        return pandoc.Para(il)
    end
end

function Math(el)
    el.text = string.gsub(el.text, "(\\pu%b{})", handlePu)
end
