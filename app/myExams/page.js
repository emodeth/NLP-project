import ExamsHeader from "@/components/ExamsHeader";
import ExamsMain from "@/components/ExamsMain";
import MaxWidthWrapper from "@/components/MaxWidthWrapper";

function ExamsPage() {
  return (
    <MaxWidthWrapper className="">
      <ExamsHeader />
      <ExamsMain>patato</ExamsMain>
    </MaxWidthWrapper>
  );
}

export default ExamsPage;
