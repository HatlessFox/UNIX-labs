cal | grep [[:cntrl:]] | sed 's@.*\x5F\x08\(.\).*\x5F\x08\(.\).*@\1\2@' | sed 's@[[:space:]]*\(.*\)@\1@'
